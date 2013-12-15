#!/usr/bin/env python
"""
NodeMeister script to show a group
"""

import optparse
import sys
import requests
import anyjson

from nodemeisterlib import *

def pprint_group(gdict, classes, params, groupnames):
    """
    pprint a group
    """
    print("Group %d '%s' (%s):" % (gdict['id'], gdict['name'], gdict['description']))
    print("  Parameters:")
    lines = []
    for p in gdict['parameters']:
        lines.append("    %s: %s" % (params[p]['paramkey'], params[p]['paramvalue']))
    for l in sorted(lines):
        print(l)
    print("  Classes:")
    lines = []
    for c in gdict['classes']:
        if classes[c]['classparams'] is None:
            v = ""
        else:
            v = ": %s" % classes[c]['classparams']
        lines.append("    %s%s" % (classes[c]['classname'], v))
    for l in sorted(lines):
        print(l)
    if len(gdict['parents']) > 0:
        print("  Parents:")
        for p in gdict['parents']:
            print("    %s (%d)" % (groupnames[p], p))
    if len(gdict['groups']) > 0:
        print("  Groups (included):")
        for g in gdict['groups']:
            print("    %s (%d)" % (groupnames[g], g))
    return

def main():
    p = optparse.OptionParser()
    p.add_option('-g', '--group', dest='group',
                 help='group name to get from dashboard')

    p.add_option('-H', '--host', dest='host', action='store', type='string',
                 help='nodemeister hostname or IP')

    options, args = p.parse_args()

    if not options.group:
        print("ERROR: you must specify a group to get with -g|--group")
        sys.exit(1)

    if not options.host:
        print("ERROR: You must specify NodeMeister Base URL with -H|--host")
        sys.exit(1)

    group_names = get_group_names(options.host)
    g_dict = get_nm_group(options.host, options.group, groupnames=group_names)
    if len(g_dict) == 0:
        sys.stderr.write("ERROR: group %s not found.\n" % options.group)
        sys.exit(1)
    classes = get_nm_group_classes(options.host)
    params = get_nm_group_params(options.host)

    pprint_group(g_dict, classes, params, group_names)

if __name__ == "__main__":
    main()
