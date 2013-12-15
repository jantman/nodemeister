"""
Some common functions for interfacing with the
NodeMeister REST API.
"""

import requests
import anyjson

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
        r[o['id']] = o
    return r

def get_nm_group(nm_host, gname=None, gid=None, groupnames=None):
    """
    Return a dict of information about a group
    in NM, by either name or ID. If fname is specified,
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
