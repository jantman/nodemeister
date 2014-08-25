#!/usr/bin/env python
"""
Simple script to list all groups and nodes that a class is applied to.
Searches a substring of the class name.
"""
import sys
import json
import requests
import os

from nodemeisterlib import get_json, get_node_names, get_group_names

usage = "USAGE: nodemeister_find_class.py nm_host class_name"

if len(sys.argv) < 3:
    print(usage)
    raise SystemExit(1)

nm_host = sys.argv[1]
cls = sys.argv[2]

if nm_host == "-h" or nm_host == "--help":
    print(usage)
    raise SystemExit(1)

print("Searching NodeMeister {nm_host} for classes containing '{cls}'".format(cls=cls, nm_host=nm_host))

nodes = get_node_names(nm_host)
groups = get_group_names(nm_host)
found = False
j = get_json("http://{nm_host}/enc/classes/nodes".format(nm_host=nm_host))
for c in j:
    if cls in c['classname']:
        found = True
        print("\tnode {node} class '{classname}' <{url}>".format(
            node=nodes[c['node']],
            classname=c['classname'],
            url="http://{nm_host}/admin/enc/node/{num}/".format(
                nm_host=nm_host,
                num=c['node'],
            ),
        ))
j = get_json("http://{nm_host}/enc/classes/groups".format(nm_host=nm_host))
for c in j:
    if cls in c['classname']:
        found = True
        print("\tgroup {group} class '{classname}' <{url}>".format(
            group=groups[c['group']],
            classname=c['classname'],
            url="http://{nm_host}/admin/enc/group/{num}/".format(
                nm_host=nm_host,
                num=c['group'],
            ),
        ))
if not found:
    print("\tnot found")
