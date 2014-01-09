#!/usr/bin/env python
"""
For use when/if transitioning from Puppet Dashboard to
NodeMeister. Retrieves the YAML file (the same one pulled
by the puppet node terminus script) for a given node from
both Dashboard and NodeMeister and compares them.
"""

from yaml import load, dump
# try to use the C-based LibYAML if we can
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import requests
import optparse
import sys

from nodemeisterlib import *

def main():
    """
    Main command-line entry method
    does option parsing, calls the other methds, prints result
    """
    usage = "USAGE: nm_dashboard_yaml_diff.py [options] -d <dashboard host> -n <nodemeister host> <node name>"
    p = optparse.OptionParser(usage=usage)

    default_dashboard_url = "https://{0}:{1}/nodes/{2}"
    p.add_option('--dashboard-url', dest='dashboard_url', action='store', type='string',
                 default=default_dashboard_url,
                 help="URL to puppet dashboard YAML for a given node, {0} " +
                 "replaced with hostname/IP {1} with the port and {2} replaced with node name\ndefault: %s" % default_dashboard_url)

    p.add_option('--dashboard-port', dest='dashboard_port', action='store', type='int',
                 help='puppet dashboard port (default 443)', default=443)

    p.add_option('--diff-only', dest='onlydifferent', action='store_true', default=False,
                 help='only output differing lines')

    p.add_option('-d', '--dashboard', dest='dashboard', action='store', type='string',
                 help='puppet dashboard hostname or IP address')

    p.add_option('-n', '--nodemeister', dest='nodemeister', action='store', type='string',
                 help='nodemeister hostname or IP address')

    p.add_option('-v', '--verbose', dest='verbose', default=False, action='store_true',
                 help='verbose output')

    options, args = p.parse_args()

    if len(args) != 1:
        print("ERROR: no node name specified\n")
        print(usage)
        sys.exit(1)
    node_name = args[0]

    if not options.nodemeister:
        print("ERROR: You must specify NodeMeister hostname/IP with -n|--nodemeister")
        sys.exit(1)

    if not options.dashboard:
        print("ERROR: You must specify Dashboard hostname/IP with -d|--dashboard")
        sys.exit(1)

    nm_yaml = get_nm_node_yaml(options.nodemeister, node_name, verbose=options.verbose)
    if nm_yaml is None:
        print("ERROR: unable to get node yaml from nodemeister at %s" % options.nodemeister)
        sys.exit(1)
    if options.verbose:
        print("NodeMeister yaml:\n%s" % nm_yaml)
    nm_node = load(nm_yaml, Loader=Loader)
    if not nm_node:
        print("ERROR loading nodemeister yaml.")
        sys.exit(1)

    dashboard_url = options.dashboard_url.format(options.dashboard, options.dashboard_port, node_name)
    dashboard_yaml = get_dashboard_node_yaml(dashboard_url, verbose=options.verbose)
    if dashboard_yaml is None:
        print("ERROR: unable to get Dashboard yaml from %s" % dashboard_url)
        sys.exit(1)
    if options.verbose:
        print("Dashboard yaml:\n%s" % dashboard_yaml)
    dash_node = load(dashboard_yaml, Loader=Loader)
    if not dash_node:
        print("ERROR loading dashboard yaml.")
        sys.exit(1)
    # Dashboard doesn't support parameterized classes, so it
    # has a list instead of a dict/hash
    dash_classes = {}
    for c in dash_node['classes']:
        dash_classes[c] = None
    dash_node['classes'] = dash_classes

    d = pretty_diff(node_name, 'dashboard', dash_node, 'nodemeister', nm_node, onlydifferent=options.onlydifferent)
    print d

    return True

if __name__ == "__main__":
    main()
