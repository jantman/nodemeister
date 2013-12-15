#!/usr/bin/env python
"""
Script to migrate a group, along with its classes and
parameters (but not nodes, parents, or child groups)
from Puppet Enterprise Console (or Dashboard?) to
NodeMeister. 

Since Console/Dashboard doesn't have a real API, this
directly accesses the MySQL database.
"""

import MySQLdb
import MySQLdb.cursors # I don't like positional refs in DB cursors
import optparse
import sys
import requests
import json

VERBOSE = False
NOOP = False

def get_group_from_dashboard(cur, groupname):
    sql = "SELECT * FROM node_groups WHERE name='%s'" % groupname
    cur.execute(sql)
    result = cur.fetchone()
    group_id = result['id']

    ret = {'params': {}, 'classes': []}

    sql = "SELECT `key`,`value` FROM parameters WHERE parameterable_type = 'NodeGroup' AND parameterable_id=%d" % group_id
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        ret['params'][row['key']] = row['value']

    sql = "SELECT nc.name FROM node_group_class_memberships AS ng LEFT JOIN node_classes AS nc ON nc.id=ng.node_class_id WHERE node_group_id=%d" % group_id
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        ret['classes'].append(row['name'])
    return ret

def get_nm_group_id(nm_host, name):
    r = requests.get("http://%s/enc/groups/" % nm_host)
    j = r.json()
    for n in j:
        if n['name'] == name:
            return n['id']
    return False

def add_group(base_url, name, description):
    """
    adds a group to NodeMeister, retrns the ID of the added group or False on failure
    """
    payload = {'name': name, 'description': description}
    headers = {'content-type': 'application/json'}
    r = requests.post("%senc/groups/" % base_url, data=json.dumps(payload), headers=headers)
    if r.status_code == 201:
        return get_group_id(base_url, name)
    return False

def add_param_to_group(base_url, gid, pname, pval):
    """
    adds a param to a group in NodeMeister, returns True on success or False on failure
    """
    if pval.strip() == "" or pval == "" or pval == "''":
        pval = None
    payload = {'group': gid, 'paramkey': pname, 'paramvalue': pval}
    headers = {'content-type': 'application/json'}
    r = requests.post("%senc/parameters/groups/" % base_url, data=json.dumps(payload), headers=headers)
    if r.status_code == 201:
        return True
    return False

def add_class_to_group(base_url, gid, classname, classparams=None):
    """
    adds a class to a group in NodeMeister, returns True on success or False on failure
    """
    payload = {'group': gid, 'classname': classname, 'classparams': classparams}
    headers = {'content-type': 'application/json'}
    r = requests.post("%senc/classes/groups/" % base_url, data=json.dumps(payload), headers=headers)
    if r.status_code == 201:
        return True
    return False

def create_nodemeister_group(base_url, group, dash_group):
    """
    Creates a group in nodemeister
    """
    gid = get_group_id(base_url, group)
    if gid is not False:
        print("ERROR: group %s already exists in NodeMeister with id %d." % (group, gid))
        return False

    # ok, try adding the group
    gid = add_group(base_url, group, "imported by pe_console_group_to_nm.py")
    if gid is False:
        print("ERROR adding group in Nodemeister.")
        return False
    else:
        print("Group added to NodeMeister with id %d" % gid)

    ok = True

    # add the params
    for p in dash_group['params']:
        res = add_param_to_group(base_url, gid, p, dash_group['params'][p])
        if not res:
            print("ERROR adding param %s with value '%s' to group %d" % (p, dash_group['params'][p], gid))
            ok = False
        if VERBOSE:
            print("\tadded param %s with value '%s' to group %d" % (p, dash_group['params'][p], gid))

    for c in dash_group['classes']:
        res = add_class_to_group(base_url, gid, c)
        if not res:
            print("ERROR adding class %s to group %d" % (c, gid))
            ok = False
        if VERBOSE:
            print("\tadded class %s to group %d" % (c, gid))

    if ok is False:
        return False
    return gid

def main():
    p = optparse.OptionParser()
    p.add_option('-g', '--group', dest='group',
                 help='group name to get from dashboard')

    p.add_option('-v', '--verbose', dest='verbose', default=False, action='store_true',
                 help='verbose output')

    p.add_option('-t', '--noop', dest='noop', default=False, action='store_true',
                 help='just print what would be done, do not update NodeMeister')

    p.add_option('-n', '--nodemeister', dest='nodemeister', action='store', type='string',
                 help='nodemeister base URL in form http://host/')

    options, args = p.parse_args()

    VERBOSE = options.verbose
    NOOP = options.noop

    if not options.group:
        print("ERROR: you must specify a group to get with -g|--group")
        sys.exit(1)

    if not options.nodemeister:
        print("ERROR: You must specify NodeMeister Base URL with -n|--nodemeister")
        sys.exit(1)

    conn = MySQLdb.connect (host = "127.0.0.1",
                            user = "puppetenterprise",
                            passwd = "puppetenterprise",
                            db = "puppetenterprise",
                            cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()

    dash_group = get_group_from_dashboard(cur, options.group)

    print("Classes:")
    for c in dash_group['classes']:
        print(" - %s" % c)
    print("\nParameters:")
    for p in dash_group['params']:
        print(" - %s : '%s'" % (p, dash_group['params'][p]))

    if not options.noop:
        res = create_nodemeister_group(options.nodemeister, options.group, dash_group)
        if res is False:
            print("Error.")
            sys.exit(1)
        else:
            print("Ok, group created with ID %d" % res)
    else:
        print("NOOP - doing nothing.")

    return 0

if __name__ == "__main__":
    main()
