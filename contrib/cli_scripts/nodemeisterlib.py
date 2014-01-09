"""
Some common functions for interfacing with the
NodeMeister REST API.
"""

import requests
import anyjson

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

def get_nm_node_yaml(nm_host, node_name, ssl_verify=False, verbose=False):
    """
    Get the raw ENC YAML for a given node

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param node_name: name of the node to get YAML for
    :type node_name: string
    :param ssl_verify: whether or not to verify SSL certificate, default False
    :type ssl_verify: boolean
    :rtype: string
    :returns: raw YAML string, or None
    """
    nm_url = "http://%s/enc/puppet/%s" % (nm_host, node_name)
    r = requests.get(nm_url, headers={'Accept': 'text/yaml'}, verify=verify)
    if r.status_code == 200:
        return r.content
    return None

def get_dashboard_node_yaml(url, ssl_verify=False, verbose=False):
    """
    Given the full URL to a Puppet Dashboard node YAML file,
    return the content of the YAML file as a string.

    :param url: full URL to Dashboard node yaml
    :type url: string
    :param ssl_verify: whether or not to verify SSL certificate, default False
    :type ssl_verify: boolean
    :rtype: string
    :returns: raw YAML string, or None
    """
    r = requests.get(url, headers={'Accept': 'text/yaml'}, verify=verify)
    if r.status_code == 200:
        return r.content
    return None

def get_json(url):
    """
    uses requests to GET and return deserialized json

    uses anyjson if the Response object doesn't have .json()

    :param url: the URL to get
    :type url: string
    :rtype: dict/mixed or None
    :returns: unserialized JSON, or None
    """
    r = requests.get(url)
    if 'json' in dir(r):
        return r.json()
    try:
        j = anyjson.deserialize(r.content)
        return j
    except:
        return None

def get_group_names(nm_host):
    """
    Return a dict of groups in the NM instance,
    id => name

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :rtype: dict
    :returns: NM groups, dict of the form {id<int>: name<string>}
    """
    j = get_json("http://%s/enc/groups/" % nm_host)
    names = {}
    for n in j:
        names[n['id']] = n['name']
    return names

def get_nm_group_classes(nm_host):
    """
    Return a dict of all group classes in NM,
    with their id as the dict key.

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :rtype: dict
    :returns: NM group classes, dict of the form:
      {id<int>: {'classname': <string>, 'classparams': <string or None>, 'group': <int>, 'id': <int>}
    """
    r = {}
    j = get_json("http://%s/enc/classes/groups/" % nm_host)
    for o in j:
        r[o['id']] = o
    return r

def get_nm_group_params(nm_host):
    """
    Return a dict of all group params in NM,
    with their id as the dict key.

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :rtype: dict
    :returns: NM group params, dict of the form:
      {id<int>: {'paramkey': <string>, 'paramvalue': <string or None>, 'group': <int>, 'id': <int>}
    """
    r = {}
    j = get_json("http://%s/enc/parameters/groups/" % nm_host)
    for o in j:
        if o['paramvalue'] is not None:
	    o['paramvalue'] = clean_value(o['paramvalue'])
        r[o['id']] = o
    return r

def get_nm_group(nm_host, gname=None, gid=None, groupnames=None):
    """
    Return a dict of information about a group
    in NM, by either name or ID. If gname is specified,
    it will be resolved to the id.

    groupnames, if specified, is the output dict from get_group_names();
    if it is not specified, get_group_names() will be called internally.

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :param gname: name of group to get
    :type gname: string
    :param gid: ID of group to get, overrides gname
    :type gid: int
    :param groupnames: output of get_group_names(), to prevent calling it again if we already have it
    :type groupnames: dict
    :rtype: dict
    :returns: unserialized JSON dict representing the specified group, of the form:
      {'name': <string>, 'parameters': [<param IDs>], 'classes': [<class IDs>], 'parents': [<group IDs>], 'groups': [<group IDs>], 'id': <int>, 'description': <string>}
    """
    if gid is None and gname is None:
        raise ValueError("get_nm_group called without gname or gid")

    if gid is None:
        if groupnames is None:
            groupnames = get_group_names(nm_host)
        for n in groupnames:
            if groupnames[n] == gname:
                gid = n
        if gid is None:
            return {}

    j = get_json("http://%s/enc/groups/%d/" % (nm_host, gid))
    return j

def interpolate_group(group, classes, params, group_names):
    """
    In the dict returned by get_nm_group, replace class
    and parameter IDs, and other group IDs, with their
    appropriate string or dict representations.

    :param group: the Group dict returned by get_nm_group()
    :type group: dict
    :param classes: the dict of classes returned by get_nm_group_classes()
    :type classes: dict
    :param params: the dict of parameters returned by get_nm_group_params()
    :type params: dict
    :param group_names: the dict of group IDs to names returned by get_group_names()
    :type group_names: dict
    :returns: group dict, with classes and params interpolated
    :rtype: dict
    """
    g_params = group.get('parameters', {})
    params_text = {}
    for p in g_params:
        foo = params[p]
        params_text[foo['paramkey']] = foo['paramvalue']
    group['parameters'] = params_text

    g_classes = group.get('classes', {})
    classes_text = {}
    for c in g_classes:
        foo = classes[c]
        classes_text[foo['classname']] = foo['classparams']
    group['classes'] = classes_text

    g_parents = group.get('parents', {})
    parents_text = []
    for p in g_parents:
        parents_text.append(group_names[p])
    group['parents'] = parents_text

    g_groups = group.get('groups', {})
    groups_text = []
    for g in g_groups:
        groups_text.append(group_names[g])
    group['groups'] = groups_text

    return group

def add_group(nm_host, name, description, parents=None, groups=None, dry_run=False):
    """
    add a group to NodeMeister

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param name: name of the new group
    :type name: string
    :param description: description of the new group
    :type description: string
    :param parents: parents of this group
    :type parents: list of int IDs
    :param groups: child groups of this group
    :type groups: list of int IDs
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: int ID of the new group on success or False on failure
    :rtype: int or False
    """
    payload = {'name': name, 'description': description}
    if parents is not None:
        payload['parents'] = parents
    if groups is not None:
        payload['groups'] = groups
    url = "http://%s/enc/groups/" % nm_host
    status_code = do_post(url, payload, dry_run=dry_run)
    if status_code == 201:
        return get_nm_group_id(nm_host, name, dry_run=dry_run)
    print("ERROR: add_group got status code %d" % status_code)
    return False

def get_nm_group_id(nm_host, name, groups=None, dry_run=False):
    """
    Get the group ID of a group specified by name

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param name: name of the new group
    :type name: string
    :param groups: dict of groups as returned by get_group_names()
    :type groups: dict
    :returns: int ID of the group or False on failure
    :rtype: int or False
    """
    if dry_run:
        return 0
    if groups is None:
        groups = get_group_names(nm_host)
    for n in groups:
        if groups[n] == name:
            return n
    return False

def add_param_to_group(nm_host, gid, pname, pval, dry_run=False):
    """
    add a parameter to a group in NodeMeister

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param gid: numeric ID of the group to add param to
    :type gid: int
    :param pname: parameter name
    :type pname: string
    :param pval: parameter value
    :type pval: string
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: True on success or False on failure
    :rtype: boolean
    """
    if pval.strip() == "" or pval == "" or pval == "''":
        pval = None
    payload = {'group': gid, 'paramkey': pname, 'paramvalue': pval}
    url = "http://%s/enc/parameters/groups/" % nm_host
    status_code = do_post(url, payload, dry_run=dry_run)
    if status_code == 201:
        return True
    print("ERROR: add_param_to_group got status code %d" % status_code)
    return False

def add_class_to_group(nm_host, gid, classname, classparams=None, dry_run=False):
    """
    add a class to a group in NodeMeister

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param gid: numeric ID of the group to add param to
    :type gid: int
    :param classname: class name
    :type classname: string
    :param classparams: class parameters, default None
    :type classparams: string or None
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: True on success or False on failure
    :rtype: boolean
    """
    payload = {'group': gid, 'classname': classname, 'classparams': classparams}
    url = "http://%s/enc/classes/groups/" % nm_host
    status_code = do_post(url, payload, dry_run=dry_run)
    if status_code == 201:
        return True
    print("ERROR: add_class_to_group got status code %d" % status_code)
    return False

def get_node_names(nm_host):
    """
    Return a dict of nodes in the NM instance,
    id => hostname

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :rtype: dict
    :returns: NM nodes, dict of the form {id<int>: hostname<string>}
    """
    j = get_json("http://%s/enc/nodes/" % nm_host)
    names = {}
    for n in j:
        names[n['id']] = n['hostname']
    return names

def get_nm_node_id(nm_host, hostname, nodenames=None, dry_run=False):
    """
    Get the node ID of a node specified by hostname

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param hostname: hostname of the node
    :type hostname: string
    :param nodenames: dict of nodes as returned by get_node_names()
    :type nodenames: dict
    :returns: int ID of the group or False on failure
    :rtype: int or False
    """
    if dry_run:
        return 0
    if nodenames is None:
        nodenames = get_node_names(nm_host)
    for n in nodenames:
        if nodenames[n] == hostname:
            return n
    return False

def get_nm_node(nm_host, hostname=None, node_id=None, nodenames=None):
    """
    Return a dict of information about a node
    in NM, by either name or ID. If nodename is specified,
    it will be resolved to the id.

    nodenames, if specified, is the output dict from get_node_names();
    if it is not specified, get_node_names() will be called internally.

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :param hostname: name of node to get
    :type hostname: string
    :param node_id: ID of node to get, overrides hostname
    :type node_id: int
    :param nodenames: output of get_node_names(), to prevent calling it again if we already have it
    :type nodenames: dict
    :rtype: dict
    :returns: unserialized JSON dict representing the specified group, of the form:
      {'hostname': <string>, 'parameters': [<param IDs>], 'classes': [<class IDs>], 'parents': [<group IDs>],
      'groups': [<group IDs>], 'id': <int>, 'description': <string>}
    """
    if node_id is None and hostname is None:
        raise ValueError("get_nm_node called without hostname or node_id")

    if node_id is None:
        if nodenames is None:
            nodenames = get_node_names(nm_host)
        for n in nodenames:
            if nodenames[n] == hostname:
                node_id = n
        if node_id is None:
            return {}

    j = get_json("http://%s/enc/nodes/%d/" % (nm_host, node_id))
    return j

def get_nm_node_classes(nm_host):
    """
    Return a dict of all node classes in NM,
    with their id as the dict key.

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :rtype: dict
    :returns: NM node classes, dict of the form:
      {id<int>: {'classname': <string>, 'classparams': <string or None>, 'node': <int>, 'id': <int>}
    """
    r = {}
    j = get_json("http://%s/enc/classes/nodes/" % nm_host)
    for o in j:
        r[o['id']] = o
    return r

def get_nm_node_params(nm_host):
    """
    Return a dict of all node params in NM,
    with their id as the dict key.

    :param nm_host: NodeMeister hostname/IP
    :type nm_host: string
    :rtype: dict
    :returns: NM node params, dict of the form:
      {id<int>: {'paramkey': <string>, 'paramvalue': <string or None>, 'node': <int>, 'id': <int>}
    """
    r = {}
    j = get_json("http://%s/enc/parameters/nodes/" % nm_host)
    for o in j:
        r[o['id']] = o
    return r

def add_node(nm_host, hostname, description, groups=None, dry_run=False):
    """
    add a node to NodeMeister

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param hostname: hostname of the new node
    :type hostname: string
    :param description: description of the new node
    :type description: string
    :param groups: groups that this node is in
    :type groups: list of int IDs
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: int ID of the new node on success or False on failure
    :rtype: int or False
    """
    payload = {'hostname': hostname, 'description': description}
    if groups is not None:
        payload['groups'] = groups
    url = "http://%s/enc/nodes/" % nm_host
    status_code = do_post(url, payload, dry_run=dry_run)
    if status_code == 201:
        return get_nm_node_id(nm_host, hostname, dry_run=dry_run)
    print("ERROR: add_node got status code %d" % status_code)
    return False

def add_param_to_node(nm_host, node_id, pname, pval, dry_run=False):
    """
    add a parameter to a node in NodeMeister

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param node_id: numeric ID of the node to add param to
    :type node_id: int
    :param pname: parameter name
    :type pname: string
    :param pval: parameter value
    :type pval: string
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: True on success or False on failure
    :rtype: boolean
    """
    if pval.strip() == "" or pval == "" or pval == "''":
        pval = None
    payload = {'node': node_id, 'paramkey': pname, 'paramvalue': pval}
    url = "http://%s/enc/parameters/nodes/" % nm_host
    status_code = do_post(url, payload, dry_run=dry_run)
    if status_code == 201:
        return True
    print("ERROR: add_param_to_node got status code %d" % status_code)
    return False

def add_class_to_node(nm_host, node_id, classname, classparams=None, dry_run=False):
    """
    add a class to a node in NodeMeister

    :param nm_host: NodeMeister hostname or IP
    :type nm_host: string
    :param node_id: numeric ID of the node to add param to
    :type node_id: int
    :param classname: class name
    :type classname: string
    :param classparams: class parameters, default None
    :type classparams: string or None
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: True on success or False on failure
    :rtype: boolean
    """
    payload = {'node': node_id, 'classname': classname, 'classparams': classparams}
    url = "http://%s/enc/classes/nodes/" % nm_host
    status_code = do_post(url, payload, dry_run=dry_run)
    if status_code == 201:
        return True
    print("ERROR: add_class_to_node got status code %d" % status_code)
    return False

def clean_value(v, debug=False):
    """
    Strip bad characters off of values
    """
    if debug:
        print("clean_value '%s'" % v)
    if type(v) == type("") or type(v) == type(u""):
        v = v.strip('"\\')
    return v

def do_post(url, payload, dry_run=False):
    """
    Do a POST request with Requests, return the status code.

    :param url: URL to POST to
    :type nm_host: string
    :param payload: the payload data, to be JSON encoded
    :type name: dict
    :param dry_run: if True, only print what would be done, do not make any changes
    :type dry_run: boolean
    :returns: HTTP status code from the request
    :rtype: int
    """
    headers = {'content-type': 'application/json'}
    if dry_run:
        print("=> DRY RUN: do_post to url %s - payload:\n\t%s\n" % (url, payload))
        return 201
    r = requests.post(url, data=anyjson.serialize(payload), headers=headers)
    return r.status_code
