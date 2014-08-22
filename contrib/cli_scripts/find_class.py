#!/usr/bin/env python

import sys
import json
import requests
import os
from optparse import OptionParser
import logging
import networkx as nx

from nodemeisterlib import get_json, get_node_names, get_group_names, get_nm_group_classes

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

def class_to_node_graph(nm_host):
    """
    loads all class, group and node data from the specified ENC instance,
    then constructs and returns a NetworkX DiGraph of the configuration,
    directed from classes to groups to nodemeister nodes

    each node in the graph has three attributes, "_id" (the ID of the object),
    "_name" (the name of the object), and "_type", a string of either "class",
    "group" or "node"

    :param nm_host: NodeMeister hostname/FQDN/IP
    :type nm_host: string
    :rtype: networkx.DiGraph
    """
    logger.debug("getting node names")
    nodes = get_node_names(nm_host)
    logger.debug("getting group names")
    groups = get_group_names(nm_host)
    logger.debug("getting group classes")
    group_classes = get_nm_group_classes(nm_host)
    logger.debug("getting group json")
    group_json = get_json("http://{nm_host}/enc/classes/groups".format(nm_host=nm_host))

    g = nx.DiGraph()

    logger.debug("getting node json")
    node_json = get_json("http://{nm_host}/enc/classes/nodes".format(nm_host=nm_host))
    logger.debug("adding nodes to graph")
    for node in node_json:
        nodename = nodes[node['node']]
        n_name = 'Node[{n}]'.format(n=nodename)
        g.add_node(n_name, _type='node', _name=nodename, _id=node['id'])
        logger.debug("adding node {n} to graph".format(n=nodename))
        for cls_name in node['classname']:
            cn_name = 'Class[{c}]'.format(c=cls_name)
            try:
                g.node[cn_name]
            except KeyError:
                g.add_node(cn_name, _type='class', _name=cls_name)
                logger.debug("adding class {c} to graph".format(c=cls_name))
            g.add_edge(cn_name, n_name)

    logger.debug("searching group json")
    for group in group_json:
        groupname = groups[group['group']]
        g_name = 'Group[{g}]'.format(g=groupname)
        g.add_node(g_name, _type='group', _name=groupname, _id=node['id'])
        logger.debug("adding group {g} to graph".format(g=groupname))
        for cls_name in group['classname']:
            raise SystemExit(cls_id)
            cls_name = group_classes[cls_id]['classname']
            cn_name = 'Class[{c}]'.format(c=cls_name)
            try:
                g.node[cn_name]
            except KeyError:
                g.add_node(cn_name, _type='class', _name=cls_name)
                logger.debug("adding class {c} to graph".format(c=cls_name))
            g.add_edge(g_name, cn_name)

    logger.debug("adding group to group associations")
    for group in group_json:
        groupname = groups[group['group']]
        g_name = 'Group[{g}]'.format(g=groupname)
        for gg in group['groups']:
            gg_name = 'Group[{gg}]'.format(gg=groups[gg])
            g.add_edge(g_name, gg_name)

    logger.debug("done creating graph")
    return g

def find_class_on_host(nm_host, class_name, out_format='text'):
    """
    find all uses of a class on a given nodemeister host

    returns a dict with keys 'groups', 'nodes' and 'all_nodes' where:
    'nodes' is a dict (id => name) of nodes with the class directly applied
    'all_nodes' is a dict (id => name) of ALL nodes with the class applied (directly or through groups)
    """
    logger.info("checking for class '{c}' on nodemeister instance: {n}".format(n=nm_host, c=class_name))
    g = class_to_node_graph(nm_host)


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
