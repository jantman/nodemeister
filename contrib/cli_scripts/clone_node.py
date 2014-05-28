#!/usr/bin/env python
"""
NodeMeister script to clone a node.

Note this is still very crude....
"""

import optparse
import sys

import requests
import anyjson

from nodemeisterlib import *

def clone_node(nm_host, src, dest, dry_run=False, verbose=False):
    """
    Clone a node
    """
    
    

def main():
    p = optparse.OptionParser()

    p.add_option('-s', '--source', dest='source', action='store', type='string',
                 help='source node hostname')

    p.add_option('-d', '--destination', dest='destination', action='store', type='string',
                 help='destination node hostname')

    p.add_option('-n', '--nodemeister', dest='nodemeister', action='store', type='string',
                 help='nodemeister hostname or IP address')

    p.add_option('--dry-run', dest='dry_run', action='store_true', default=False,
                 help="dry run - don't actually do anything, just print what would be done")

    p.add_option('-v', '--verbose', dest='verbose', default=False, action='store_true',
                 help='verbose output')

    options, args = p.parse_args()

    if not options.source or not options.destination:
        print("ERROR: you must specify both a source (-s|--source) and destination (-d|--destionation) node name")
        sys.exit(1)

    res = clone_nodemeister_node(options.nodemeister, options.destination, options.source, [], None, options.dry_run, options.verbose)
    print res

if __name__ == "__main__":
    main()
