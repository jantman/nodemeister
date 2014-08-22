#!/usr/bin/env python

import sys
import json
import requests
import os
from optparse import OptionParser
import logging

from nodemeisterlib import get_json, get_node_names, get_group_names

FORMAT = "[%(levelname)s %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger(__name__)

def format_output_text(result_dict):
    """ formats result_dict for textual (human-readable) output """
    print(result_dict)

def format_output_files(result_dict):
    """ formats result_dict as one file per NM host, one hostname per line """
    print(result_dict)

def find_class(nm_hosts, class_name, out_format='text'):
    """
    find all uses of a specified class on the specified NodeMeister host(s)

    :param nm_hosts: list of NodeMeister hostname/FQDN/IP(s) to search
    :type nm_hosts: list of strings
    """
    logger.info("searching for class {c}".format(c=class_name))
    formats = {'text': format_output_text, 'files': format_output_files}
    if out_format not in formats.keys():
        raise SystemExit("ERROR: output format must be one of: {f}".format(f=", ".join(formats)))

    results = {}
    for host in nm_hosts:
        results[host] = find_class_on_host(host, class_name)

    logger.info("finished searching; formatting output as '{o}'".format(o=out_format))
    formats[out_format](results)

def find_class_on_host(nm_host, class_name, out_format='text'):
    """
    find all uses of a class on a given nodemeister host

    returns a dict with keys 'groups', 'nodes' and 'all_nodes' where:
    'nodes' is a dict (id => name) of nodes with the class directly applied
    'all_nodes' is a dict (id => name) of ALL nodes with the class applied (directly or through groups)
    """
    logger.info("checking for class '{c}' on nodemeister instance: {n}".format(n=nm_host, c=class_name))
    logger.debug("getting node names")
    nodes = get_node_names(nm_host)
    logger.debug("getting group names")
    groups = get_group_names(nm_host)
    results = {'groups': {}, 'nodes': {}, 'all_nodes': {}}
    tmp_groups = {}
    logger.debug("getting group json")
    group_json = get_json("http://{nm_host}/enc/classes/groups".format(nm_host=nm_host))
    logger.debug("searching group json")
    for group in group_json:
        groupname = groups[group['group']]
        if class_name in group['classname']:
            logger.debug("found class in group {g}".format(g=groupname))
            results['groups'][groupname] = {'groups': {}, 'nodes': {}}
            for g in group['groups']:
                results['groups'][groupname][groups][g] = {}
                tmp_groups[g] = {}
    logger.debug("getting node json")
    node_json = get_json("http://{nm_host}/enc/classes/nodes".format(nm_host=nm_host))
    logger.debug("searching node json")
    for node in node_json:
        nodename = nodes[node['node']]
        if class_name in node['classname']:
            logger.debug("found class on node {n}".format(n=nodename))
            results['nodes'][node['id']] = nodename
            results['all_nodes'][node['id']] = nodename
        for g in 

    logger.debug("done searching {n}; returning result dict".format(n=nm_host))
    return results

def parse_opts_args(argv):
    """ parse options and arguments """
    usage = "USAGE: find_class.py [options] class_name"
    p = OptionParser(usage=usage)

    p.add_option('-v', '--verbose', dest='verbose', action='count', default=0,
                 help='verbose output. specify twice for debug-level output.')

    p.add_option('-n', '--nodemeister', dest='nm_host', action='append',
                 help='nodemeister hostname/FQDN/IP; specify multiple times to search multiple instances')

    p.add_option('-o', '--output-format', dest='out_format', action='store', type='string', default='text',
                 help='output format; "text" for human-readable text (default) or "files" for one file per nodemeister listing hostnames')

    (options, args) = p.parse_args(argv)
    return (options, args)

if __name__ == "__main__":
    (opts, args) = parse_opts_args(sys.argv[1:])

    if opts.verbose > 1:
        logger.setLevel(logging.DEBUG)
        logger.debug("Running with DEBUG level logging...")
    elif opts.verbose > 0:
        logger.setLevel(logging.INFO)
        logger.info("Running with INFO level logging...")

    if len(args) != 1:
        raise SystemExit("ERROR: you must specify exactly one argument (class name to search for)")

    cls = args[0]
    find_class(opts.nm_host, cls, out_format=opts.out_format)
