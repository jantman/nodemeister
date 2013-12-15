#!/usr/bin/env python
"""
NodeMeister script to migrate changes between
NodeMiester instances, showing a diff before
committing changes.

Note this is still very crude....
"""

import optparse
import sys

import requests
import anyjson

from nodemeisterlib import *

MISSING_ITEM = '-'
DIFF_MARKER = ">"

def red(text):
    """
    Shameless hack-up of the 'termcolor' python package
    by Konstantin Lepa - <https://pypi.python.org/pypi/termcolor>
    to reduce rependencies and only make red text.
    """
    s = '\033[%dm%s\033[0m' % (31, text)
    return s

def print_columns(lines, spacer='   '):
    """
    Take a list of lines, each being a list with 3 elements
    (the three columns to print) and print in 3 columns.

    :param lines: list of 3-element lists, each list is a line and
    each sub-list are the 3 columns in the line
    :type lines: list of lists
    :param spacer: spacer between columns, default 3 spaces
    :type lines: string
    """
    s = ""
    # get the column width
    clen = [0, 0, 0]
    for l in lines:
        for c in xrange(0, 3):
            if len(str(l[c])) > clen[c]:
                clen[c] = len(str(l[c]))
    line_spec = "{{0:<{1}s}}{0}{{1:<{2}s}}{0}{{2:<{3}s}}\n".format(' ' * 3, clen[0], clen[1], clen[2])

    # print the lines
    for l in lines:
        if len(l) > 3 and l[3] == True:
            s += red(line_spec.format(DIFF_MARKER + l[0], l[1], l[2]))
        else:
            s += line_spec.format(l[0], str(l[1]), str(l[2]))
    return s

def pretty_diff_list(title, oA, oB):
    """
    Generate a pretty diff of two dicts.

    :param title: the title/heading for the line
    :type title: string
    :param oA: first object
    :param oB: second object
    :returns: list of lines, each a list of 3 columns
    :rtype: list of lists
    """
    lines = []
    items = set.union(set(oA), set(oB))
    for i in sorted(items):
        if i in oA and i in oB:
            lines.append(['', i, i])
        elif i in oA:
            lines.append(['', i, MISSING_ITEM, True])
        elif i in oB:
            lines.append(['', MISSING_ITEM, i, True])
    return lines

def pretty_diff_str(title, oA, oB):
    """
    Generate a pretty diff of two dicts.

    :param title: the title/heading for the line
    :type title: string
    :param oA: first object
    :param oB: second object
    :returns: list of lines, each a list of 3 columns
    :rtype: list of lists
    """
    if oA != oB:
        return [[title, oA, oB, True]]
    return [[title, oA, oB]]

def pretty_diff_dict(title, oA, oB):
    """
    Generate a pretty diff of two dicts.

    :param title: the title/heading for the line
    :type title: string
    :param oA: first object
    :param oB: second object
    :returns: list of lines, each a list of 3 columns
    :rtype: list of lists
    """
    lines = [[title, '', '']]

    keys = set.union(set(oA.keys()), set(oB.keys()))

    for k in sorted(keys):
        if k in oA and k in oB:
            if oA[k] == oB[k]:
                lines.append([k, oA[k], oB[k]])
            else:
                lines.append([k, oA[k], oB[k], True])
        elif k in oA:
            lines.append([k, oA[k], MISSING_ITEM, True])
        else:
            lines.append([k, MISSING_ITEM, oB[k], True])

    return lines

def pretty_diff_obj(title, oA, oB):
    """
    Generate a pretty diff of two objects (actually just
    dict, list or string) of lines suitable for use in pretty_diff_dicts()

    This method is a pass-through to
    pretty_diff_(dict|string|list)
    depending on the input type.

    :param title: the title/heading for the line
    :type title: string
    :param oA: first object
    :param oB: second object
    :returns: list of lines, each a list of 3 columns
    :rtype: list of lists
    """
    if type(oA) == type({}) or type(oB) == type({}):
        return pretty_diff_dict(title, oA, oB)
    elif type(oA) == type("") or type(oB) == type("") or type(oA) == type(u"") or type(oB) == type(u""):
        return pretty_diff_str(title, oA, oB)
    else:
        return pretty_diff_list(title, oA, oB)
    return []

def pretty_diff(title, titleA, dictA, titleB, dictB):
    """
    Generate a "pretty" printable diff of two Nodes or Groups
    containing arbitrarily deep dict, list or string items.

    Intended to be used for the "text" dicts in migrate_group()
    and migrate_node().

    :param title: overall title of the diff
    :type title: string
    :param titleA: title of the first dict
    :type titleA: string
    :param dictA: the first dict
    :type dictA: dict
    :param titleB: title of the second dict
    :type titleB: string
    :param dictB: the second dict
    :type dictB: dict
    :returns: multi-line string, columnar diff of dicts
    :rtype: string
    """
    s = "Diff of %s\n" % title
    lines = []
    lines.append(['', titleA, titleB])
    lines.append(['', '-' * len(titleA), '-' * len(titleB)])

    lines.append(['name', dictA.get('name', '<none>'), dictB.get('name', '<none>')])
    lines.append(['id', dictA.get('id', '<none>'), dictB.get('id', '<none>')])
    lines.append(['description', dictA.get('description', '<none>'), dictB.get('description', '<none>')])
    dictA.pop('name', None)
    dictA.pop('id', None)
    dictA.pop('description', None)
    dictB.pop('name', None)
    dictB.pop('id', None)
    dictB.pop('description', None)
    lines.append(['', '', ''])

    k = set.union(set(dictA.keys()), set(dictB.keys()))
    
    for p in sorted(k):
        lines.append([p.capitalize() + ':', '', ''])
        lines.extend(pretty_diff_obj('', dictA.get(p), dictB.get(p)))
        lines.append(['', '', ''])

    s += print_columns(lines)
    return s

def migrate_group(name, src, dest, dry_run=True, batchmode=True):
    """
    Migrate a group from src NodeMeister to dest NodeMeister.

    If dry_run is True, only show a diff, do not make changes.

    If batchmode is True, don't show a diff or ask for input,
    just make the changes if possible, regardless of current state.

    :param name: the group name to migrate
    :type name: string
    :param src: the source NodeMeister hostname/IP
    :type src: string
    :param dest: the destination NodeMeister hostname/IP
    :type dest: string
    :param dry_run: if True only show what changes would be made, else actually migrate
    :type dry_run: boolean
    :param batchmode: whether or not to show diff and prompt for batchmode confirmation
    :type batchmode: boolean
    :rtype: int or False
    :returns: int group ID if migration was successful, otherwise False
    """

    # cache some commonly used stuff so we only call it once
    s_group_names = get_group_names(src)
    d_group_names = get_group_names(dest)
    s_classes = get_nm_group_classes(src)
    s_params = get_nm_group_params(src)
    d_classes = get_nm_group_classes(dest)
    d_params = get_nm_group_params(dest)

    s_g = get_nm_group(src, name, groupnames=s_group_names)
    d_g = get_nm_group(dest, name, groupnames=d_group_names)
    s_g_text = interpolate_group(s_g, s_classes, s_params, s_group_names)
    d_g_text = interpolate_group(d_g, d_classes, d_params, d_group_names)

    if d_g == {} or d_g == {'classes': {}, 'parents': [], 'groups': [], 'parameters': {}}:
        d_g = {}
        print("Group '%s' not present on destination instance (%s)." % (name, dest))
    else:
        diff = pretty_diff("Group '%s'" % name, src, s_g_text, dest, d_g_text)
        print diff

    if not batchmode:
        if dry_run:
            print("DRY RUN MODE - will not make changes. Run with '-m|--migrate' to make changes.")
        foo = raw_input("Continue with migration from %s to %s? [y|N]" % (src, dest))
        if foo not in ['y', 'Y', 'yes']:
            print("OK, aborting.")
            return False
    # else just continue and do it

    if d_g == {}:
        # doesn't exist on destination yet, create from scratch
        create_new_group(dest, s_g_text, dry_run=dry_run)
    else:
        print("ERROR: group update/change not implemented yet")

    return False

def create_new_group(nm_host, g_dict, group_names=None, dry_run=True):
    """
    Create a new group on nm_host matching g_dict,
    the information gathered in migrate_group. g_dict
    should be interoplated with string values in place
    of IDs, i.e. it should be the output of get_nm_group()
    passed through interpolate_group().

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param g_dict: dict of group information
    :type g_dict: dict
    :param group_names: output of get_group_names(nm_host)
    :type group_names: dict
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: True on success, False otherwise
    :rtype: boolean
    """
    if group_names is None:
        group_names = get_group_names(nm_host)
    group_ids = {}
    for i in group_names:
        group_ids[group_names[i]] = i

    if g_dict['name'] in group_names:
        print("ERROR: group %s already exists. Failing. (%s)" % (g_dict['name'], nm_host))
        return False

    parents = []
    for g in g_dict['parents']:
        if g in group_ids:
            parents.append(group_ids[g])
        else:
            print("WARNING: group '%s' parent group '%s' does not exist yet, you must manually create this relationship." % (g_dict['name'], g))

    groups = []
    for g in g_dict['groups']:
        if g in group_ids:
            groups.append(group_ids[g])
        else:
            print("WARNING: group '%s' child group '%s' does not exist yet, you must manually create this relationship." % (g_dict['name'], g))

    gid = add_group(nm_host, g_dict['name'], g_dict['description'], parents=parents, groups=groups, dry_run=dry_run)
    if gid is False:
        print("ERROR: Adding new group %s failed. (%s)" % (g_dict['name'], nm_host))
        return False
    print("Added new group %s (id %s). (%s)" % (g_dict['name'], gid, nm_host))

    for pname in g_dict['parameters']:
        res = add_param_to_group(nm_host, gid, pname, g_dict['parameters'][pname], dry_run=dry_run)
        if res is False:
            print("ERROR: Adding param '%s' with value '%s' to group '%s' (%d) failed. (%s)" % (pname, g_dict['parameters'][pname], g_dict['name'], gid, nm_host))
            return False
        print("Added param '%s' with value '%s' to group '%s' (%d). (%s)" % (pname, g_dict['parameters'][pname], g_dict['name'], gid, nm_host))

    for cname in g_dict['classes']:
        res = add_class_to_group(nm_host, gid, cname, g_dict['classes'][cname], dry_run=dry_run)
        if res is False:
            print("ERROR: Adding class '%s' with params '%s' to group '%s' (%d) failed. (%s)" % (cname, g_dict['classes'][cname], g_dict['name'], gid, nm_host))
            return False
        print("Added class '%s' with params '%s' to group '%s' (%d). (%s)" % (cname, g_dict['classes'][cname], g_dict['name'], gid, nm_host))

    return True

def migrate_node(name, src, dest, dry_run=True, batchmode=True):
    """
    Migrate a node from src NodeMeister to dest NodeMeister.

    If dry_run is True, only show a diff, do not make changes.

    If batchmode is True, don't show a diff or ask for input,
    just make the changes if possible, regardless of current state.

    :param name: the node name to migrate
    :type name: string
    :param src: the source NodeMeister hostname/IP
    :type src: string
    :param dest: the destination NodeMeister hostname/IP
    :type dest: string
    :param dry_run: if True only show what changes would be made, else actually migrate
    :type dry_run: boolean
    :param batchmode: whether or not to show diff and prompt for batchmode confirmation
    :type batchmode: boolean
    :rtype: int or False
    :returns: int node ID if migration was successful, otherwise False
    """
    print("ERROR: migrate_node not implemented.")
    return False

def main():
    p = optparse.OptionParser()

    p.add_option('-s', '--source', dest='source', action='store', type='string',
                 help='source nodemeister hostname or IP')

    p.add_option('-d', '--destination', dest='destination', action='store', type='string',
                 help='destination nodemeister hostname or IP')

    p.add_option('-g', '--group', dest='group', action='store', type='string',
                 help='node name to migrate')

    p.add_option('-n', '--node', dest='node', action='store', type='string',
                 help='node name to migrate')

    p.add_option('-m', '--migrate', dest='migrate', action='store_true', default=False,
                 help='migrate the data (otherwise just show the diff')

    p.add_option('-b', '--batch', dest='batch', action='store_true', default=False,
                 help="batch mode - don't show diffs or ask for interactive confirmation, just do it")

    options, args = p.parse_args()

    if not options.source or not options.destination:
        print("ERROR: you must specify both a source (-s|--source) and destination (-d|--destionation) NodeMeister host")
        sys.exit(1)

    if (not options.group and not options.node) or (options.group and options.node):
        print("ERROR: you must specify either a group (-g|--group) or a node (-n|--node) name to migrate")
        sys.exit(1)

    if options.node:
        migrate_node(options.node, src=options.source, dest=options.destination, dry_run=(not options.migrate), batchmode=options.batch)
    else:
        migrate_group(options.group, src=options.source, dest=options.destination, dry_run=(not options.migrate), batchmode=options.batch)

if __name__ == "__main__":
    main()
