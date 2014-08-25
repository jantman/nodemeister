#!/usr/bin/env python

import sys
import json
import requests
import os
from optparse import OptionParser
import logging
import networkx as nx
from collections import defaultdict

from nodemeisterlib import get_json, get_node_names, get_group_names, get_nm_group_classes

FORMAT = "[%(levelname)s %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger(__name__)

def format_output_text(result_dict):
    """ formats result_dict for textual (human-readable) output """
    for host in result_dict:
        print("#### {h} ####".format(h=host))
        for c in result_dict[host]['not_found']:
            logger.error("Class '{c}' not found anywhere on host {h}".format(h=host, c=c))
        sources = defaultdict(list)
        for node in result_dict[host]['endpoints']:
            rn = result_dict[host]['endpoints'][node]
            if rn['_type'] == 'group':
                k = "Group '{n}'".format(n=rn['_name'])
            elif rn['_type'] == 'class':
                k = "Direct (class '{n}')".format(n=rn['_name'])
            else:
                k = "{t} {n}".format(t=rn['_type'], n=rn['_name'])
            sources[k].append(node)
        for k in sorted(sources.keys()):
            print(k)
            for v in sorted(sources[k]):
                print("\t{v}".format(v=v))
    return True

def format_output_files(result_dict):
    """ formats result_dict as one file per NM host, one hostname per line """
    for host in result_dict:
        fname = host
        nf_fname = "{f}_not_found".format(f=fname)
        logger.warning("writing results for {h} to {f}".format(h=host, f=fname))
        with open(fname, 'w') as fh:
            for node in sorted(result_dict[host]['endpoints']):
                fh.write("{n}\n".format(n=node))
        logger.warning("writing not_found results for {h} to {f}".format(h=host, f=nf_fname))
        with open(nf_fname, 'w') as fh:
            for c in result_dict[host]['not_found']:
                logger.error("Class '{c}' not found anywhere on host {h}".format(h=host, c=c))
                fh.write("{c}\n".format(c=c))
    return True

def find_classes(nm_hosts, class_names, out_format='text', use_pickle=False):
    """
    find all uses of a specified class(es) on the specified NodeMeister host(s)

    :param nm_hosts: list of NodeMeister hostname/FQDN/IP(s) to search
    :type nm_hosts: list of strings
    :param class_names: list of class names to search for
    :type class_names: list
    :param use_pickle: if true, write graph to a pickle file if it does not exist; read
    from pickle file (instead of live API) if it does
    :type use_pickle: boolean
    """
    logger.info("searching for class(es) {c}".format(c=class_names))
    formats = {'text': format_output_text, 'files': format_output_files}
    if out_format not in formats.keys():
        raise SystemExit("ERROR: output format must be one of: {f}".format(f=", ".join(formats)))

    results = {}
    for host in nm_hosts:
        results[host] = find_classes_on_host(host, class_names, use_pickle=use_pickle)

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

    g = nx.DiGraph()

    logger.debug("adding groups to graph")
    for group in groups:
        groupname = groups[group]
        g_name = 'Group[{g}]'.format(g=groupname)
        logger.debug("adding group {g} to graph".format(g=groupname))
        g.add_node(g_name, _type='group', _name=groupname, _id=group)

    logger.debug("getting node json")
    node_json = get_json("http://{nm_host}/enc/nodes".format(nm_host=nm_host))
    logger.debug("adding node groups to graph")
    for node in node_json:
        nodename = node['hostname']
        n_name = 'Node[{n}]'.format(n=nodename)
        logger.debug("adding node {n} to graph".format(n=nodename))
        g.add_node(n_name, _type='node', _name=nodename, _id=node['id'])
        for g_id in node['groups']:
            g_name = 'Group[{g}]'.format(g=groups[g_id])
            logger.debug("adding edge {n} -> {g}".format(n=n_name, g=g_name))
            g.add_edge(n_name, g_name)

    logger.debug("getting node classes json")
    node_json = get_json("http://{nm_host}/enc/classes/nodes".format(nm_host=nm_host))
    logger.debug("adding nodes to graph")
    for node in node_json:
        nodename = nodes[node['node']]
        n_name = 'Node[{n}]'.format(n=nodename)
        cls_name = node['classname']
        cn_name = 'Class[{c}]'.format(c=cls_name)
        try:
            g.node[cn_name]
        except KeyError:
            logger.debug("adding class {c} to graph".format(c=cls_name))
            g.add_node(cn_name, _type='class', _name=cls_name)
        logger.debug("adding edge {c} -> {n}".format(c=cn_name, n=n_name))
        g.add_edge(n_name, cn_name)

    logger.debug("adding group classes")
    for gc in group_classes:
        g_name = 'Group[{g}]'.format(g=groups[group_classes[gc]['group']])
        c_name = 'Class[{c}]'.format(c=group_classes[gc]['classname'])
        try:
            g.node[c_name]
        except KeyError:
            logger.debug("adding class {c} to graph".format(c=group_classes[gc]['classname']))
            g.add_node(c_name, _type='class', _name=group_classes[gc]['classname'])
        logger.debug("adding edge {g} -> {c}".format(g=g_name, c=c_name))
        g.add_edge(g_name, c_name)

    logger.debug("getting group json")
    group_json = get_json("http://{nm_host}/enc/groups/".format(nm_host=nm_host))
    logger.debug("adding group to group associations")
    for group in group_json:
        groupname = group['name']
        g_name = 'Group[{g}]'.format(g=groupname)
        for gg in group['groups']:
            gg_name = 'Group[{gg}]'.format(gg=groups[gg])
            logger.debug("adding edge {g} -> {gg}".format(g=g_name, gg=gg_name))
            g.add_edge(g_name, gg_name)

    logger.debug("done creating graph")
    return g

def find_classes_on_host(nm_host, class_names, out_format='text', use_pickle=False):
    """
    find all uses of a class(es) on a given nodemeister host

    returns a dict with two keys, 'endpoints' (a dict of node to endpoint) and
    'not_found', a list of class names not found anywhere in the graph
    """
    picklefile = "graph_{h}.pickle".format(h=nm_host)
    if use_pickle:
        logger.debug("running with use_pickle=True")
        if os.path.exists(picklefile):
            logger.warning("Not getting live data; using pickled data from {pf}".format(pf=picklefile))
            g = nx.read_gpickle(picklefile)
        else:
            g = class_to_node_graph(nm_host)
            logger.warning("Pickling graph to {pf}".format(pf=picklefile))
            nx.write_gpickle(g, picklefile)
    rg = g.reverse()
    result = {}
    not_found = []
    for class_name in class_names:
        logger.info("checking for class '{c}' on nodemeister instance: {n}".format(n=nm_host, c=class_name))

        c_name = 'Class[{c}]'.format(c=class_name)
        try:
            g.node[c_name]
        except KeyError:
            not_found.append(class_name)
            logger.error("ERROR: class {c} not found anywhere in graph.".format(c=class_name))
            continue

        logger.debug("searching graph for endpoints connected to {c}".format(c=c_name))

        endpoints = nx.algorithms.traversal.depth_first_search.dfs_predecessors(rg, c_name)
        for e in endpoints:
            if rg.node[e]['_type'] == 'node':
                result[rg.node[e]['_name']] = rg.node[endpoints[e]]
    return {'endpoints': result, 'not_found': not_found}

def parse_opts_args(argv):
    """ parse options and arguments """
    usage = "USAGE: find_class.py [options] class_name [[class_name] ...]"
    p = OptionParser(usage=usage)

    p.add_option('-v', '--verbose', dest='verbose', action='count', default=0,
                 help='verbose output. specify twice for debug-level output.')

    p.add_option('-n', '--nodemeister', dest='nm_host', action='append',
                 help='nodemeister hostname/FQDN/IP; specify multiple times to search multiple instances')

    p.add_option('-o', '--output-format', dest='out_format', action='store', type='string', default='text',
                 help='output format; "text" for human-readable text (default) or "files" for one file per nodemeister listing hostnames')

    p.add_option('-p', '--pickle', dest='pickle_path', action='store_true', default=False,
                 help='store graph to pickle file; read from file if it exists')

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

    if len(args) < 1:
        raise SystemExit("ERROR: you must specify one or more arguments (class name to search for)")

    cls = args[0:]
    use_pickle = False
    if opts.pickle_path:
        use_pickle = True
    find_classes(opts.nm_host, cls, out_format=opts.out_format, use_pickle=use_pickle)
