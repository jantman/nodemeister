from collections import namedtuple
from models import *


def get_exclusions(node):
    excluded_groups = get_excluded_groups(node)
    excluded_classes = get_excluded_classes(node)
    excluded_params = get_excluded_params(node)
    return {"groups": excluded_groups,
            "classes": excluded_classes, "params": excluded_params}


def get_excluded_groups(node):
    excluded_groups = []
    for group_exclusion in node.excluded_groups.all():
        excluded_groups.append(group_exclusion.name)
    return excluded_groups


def get_excluded_classes(node):
    excluded_classes = []
    for class_exclusion in node.excluded_classes.all():
        excluded_classes.append(class_exclusion.exclusion)
    return excluded_classes


def get_excluded_params(node):
    excluded_params = []
    for param_exclusion in node.excluded_params.all():
        excluded_params.append(param_exclusion.exclusion)
    return excluded_params


def walk_tree(obj, **kwargs):
    exclusions = kwargs.get('exclusions',
                            {"groups": [],
                             "classes": [],
                             "params": []})
    groups_done = kwargs.get('groups_done', [])
    classes = kwargs.get('classes', {})
    params = kwargs.get('params', {})

    if hasattr(obj, 'name'):
        if (obj.name in groups_done):
            return (classes, params)
        groups_done.append(obj.name)
    for group in obj.groups.exclude(name__in=exclusions['groups'] + groups_done):
        walk_tree(group, exclusions=exclusions,
                  classes=classes, params=params, groups_done=groups_done)

    objclasses = obj.classes.exclude(classname__in=exclusions['classes'])
    update_values(objclasses, "classname", "classparams", results=classes)

    objparams = obj.parameters.exclude(paramkey__in=exclusions['params'])
    update_values(objparams, "paramkey", "paramvalue", results=params)

    params['done_count'] = len(groups_done)
    return (classes, params)


# functions from performance testing
def just_work_tree(obj, **kwargs):
    to_index = [(obj, 0)]
    while to_index:
        (obj, depth) = to_index.pop()
        for group in obj.groups.iterator():
            to_index.append((group, depth + 1))


def just_walk_tree(obj, **kwargs):
    groups_done = []
    for group in obj.groups.all().select_related('groups'):
        just_walk_tree(group)
    return ()


def update_values(objs, keyname, valuename, **kwargs):
    depth = kwargs.get("depth", False)
    if not depth:
        results = kwargs.get("results", {})
    else:
        results = kwargs.get("results", {"depths": {}, "content": {}})
    for obj in objs:
        if hasattr(obj, keyname):
            keyinstance = getattr(obj, keyname)
            if not depth:
                results[keyinstance] = getattr(obj, valuename, None)
            else:
                if keyinstance in results["depths"] and results["depths"][keyinstance] == depth:
                    print results
                    return False
                if keyinstance not in results["depths"] or results["depths"][keyinstance] > depth:
                    results["depths"][keyinstance] = depth
                    results["content"][keyinstance] = getattr(obj, valuename, None)
    return True


def work_tree(obj, **kwargs):
    """
    This appears to be totally unused, and leftover from testing.
    It may, in fact, be better/more efficient than the used walk_tree() method.
    """
    max_depth = 0
    exclusions = kwargs.get('exclusions', {"groups": [], "classes": [], "params": []})
    groups_done = {}
    classes = {"depths": {}, "content": {}}
    params = {"depths": {}, "content": {}}
    if hasattr(obj, 'hostname') and not hasattr(obj, 'name'):
        obj.name = obj.hostname
    to_index = [(obj, 1)]

    while to_index:
        (obj, depth) = to_index.pop()
        if obj.name in groups_done and groups_done[obj.name] <= depth:
            continue

        objclasses = obj.classes.exclude(classname__in=exclusions['classes'])
        updated_classes = update_values(objclasses, "classname", "classparams", depth=depth, results=classes)

        objparams = obj.parameters.exclude(paramkey__in=exclusions['params'])
        updated_params = update_values(objparams, "paramkey", "paramvalue", depth=depth, results=params)

        if not updated_classes or not updated_params:
            return ("Fail", "Fail")

        groups_done[obj.name] = depth
        depth += 1
        for group in obj.groups.exclude(name__in=exclusions['groups']):
            to_index.append((group, depth))
            if max_depth < depth:
                max_depth = depth

    params["content"]['max_depth'] = max_depth
    params["content"]['done_count'] = len(groups_done)
    return (classes["content"], params["content"])


def get_host_data(hostname, gettype='walk'):
    """
    Return data (tuple of classes, params) for a given host.
    """
    filteredNodes = Node.objects.filter(hostname=hostname)
    if (filteredNodes.count() == 1):
        node = filteredNodes[0]
        exclusions = get_exclusions(node)
        if gettype == 'work':
            (classes, params) = work_tree(node, exclusions=exclusions)
            return (classes, params)
        elif gettype == 'optwork':
            (classes, params) = optimized_work_tree(node, exclusions=exclusions)
            return (classes, params)
        elif gettype == 'classwork':
            (classes, params) = work_tree2(node, exclusions=exclusions)
            return (classes, params)
        elif gettype == 'walk':
            (classes, params) = walk_tree(node, exclusions=exclusions)
            return (classes, params)
    else:
        return ({}, {})


def add_node(**kwargs):
    node = Node()
    for key, value in kwargs.iteritems():
        if key in node.__dict__:
            node.__dict__[key]
    node.save()
    return node.id


Exclusions = namedtuple('Exclusions', ('groups', 'classes', 'params'))
NodeEntry = namedtuple('NodeEntry', ('key', 'value', 'depth'))


class NodeResults(object):
        __slots__ = ('entries', 'nodetype')

        def __init__(self, entries=None, nodetype='unspecified'):
                self.entries = entries if entries is not None else {}
                self.nodetype = nodetype

        def add_entry(self, key, value, depth):
                """Adds a node entry definition if there is no lower depth definition.
                Raises RuntimeError if the depth matches."""
                current = self.entries.get(key, None)
                if current is None or current.depth > depth:
                        self.entries[key] = NodeEntry(key, value, depth)
                elif current.depth == depth:
                        raise RuntimeError('Collision [depth=%d] for entry [type=%s]: %s' % (depth, self.nodetype, key))

        def add_entries(self, objs, keyname, valuename, depth):
                """Adds all the entries in objs at the current depth."""
                add_entry = self.add_entry
                for obj in objs:
                        key = getattr(obj, keyname, None)
                        if key is None:
                            continue
                        value = getattr(obj, valuename, None)
                        add_entry(key, value, depth)

        def as_dict(self):
                """Returns the entries as a key => value dict."""
                return dict((key, value) for key, value, depth in self.entries.itervalues())


def work_tree2(obj, **kwargs):
    """
    This appears to be totally unused, and leftover from testing.
    It may, in fact, be better/more efficient than the used walk_tree() method.
    """
    if 'exclusions' in kwargs:
        exclusions = kwargs['exclusions']
    else:
        exclusions = Exclusions([], [], [])
    #groups_done = {}
    classes = NodeResults(nodetype='classes')
    params = NodeResults(nodetype='params')
    if hasattr(obj, 'hostname') and not hasattr(obj, 'name'):
        obj.name = obj.hostname
    to_index = [(obj, 1)]

    # loop opts
    index_pop = to_index.pop
    index_extend = to_index.extend
    egroups, eclasses, eparams = exclusions
    add_classes = classes.add_entries
    add_params = params.add_entries

    while to_index:
        (obj, depth) = index_pop()
        #objname = obj.name
        #if objname in groups_done and groups_done[objname] <= depth:
        #continue
        try:
            objclasses = obj.classes.exclude(classname__in=eclasses)
            add_classes(objclasses, "classname", "classparams", depth)
            objparams = obj.parameters.exclude(paramkey__in=eparams)
            add_params(objparams, "paramkey", "paramvalue", depth)
        except RuntimeError, e:
            return ("Fail", "Fail")  # or just let it bubble up to the caller

        #groups_done[objname] = depth
        depth += 1
        children = [(group, depth) for group in obj.groups.exclude(name__in=egroups)]
        index_extend(children)

    return classes.as_dict(), params.as_dict()  # or (classes.entries, params.entries)


## Below are micro-optimized versions of work_tree and update_values submitted by jcobb
def optimized_work_tree(obj, **kwargs):
    """
    This appears to be totally unused, and leftover from testing.
    It may, in fact, be better/more efficient than the used walk_tree() method.
    """
    exclusions = kwargs.get('exclusions', {"groups": [], "classes": [], "params": []})
    groups_done = {}
    classes = {"depths": {}, "content": {}}
    params = {"depths": {}, "content": {}}
    if hasattr(obj, 'hostname') and not hasattr(obj, 'name'):
        obj.name = obj.hostname
    to_index = [(obj, 1)]

    index_pop = to_index.pop
    index_extend = to_index.extend
    while to_index:
        (obj, depth) = index_pop()
        objname = obj.name
        if objname in groups_done and groups_done[objname] <= depth:
            continue

        objclasses = obj.classes.exclude(classname__in=exclusions['classes'])
        updated_classes = optimized_update_values(objclasses, "classname", "classparams", depth=depth, results=classes)

        objparams = obj.parameters.exclude(paramkey__in=exclusions['params'])
        updated_params = optimized_update_values(objparams, "paramkey", "paramvalue", depth=depth, results=params)

        if not updated_classes or not updated_params:
            return ("Fail", "Fail")

        groups_done[objname] = depth
        depth += 1
        children = ((group, depth) for group in obj.groups.exclude(name__in=exclusions['groups']))
        index_extend(children)

    params['content']['done_count'] = len(groups_done)
    return (classes["content"], params["content"])


def optimized_update_values(objs, keyname, valuename, **kwargs):
    depth = kwargs.get("depth", False)
    if not depth:
        results = kwargs.get("results", {})
    else:
        results = kwargs.get("results", {"depths": {}, "content": {}})
    depths = results["depths"]
    content = results["content"]
    for obj in objs:
        if hasattr(obj, keyname):
            keyinstance = getattr(obj, keyname)
            if not depth:
                results[keyinstance] = getattr(obj, valuename, None)
            else:
                if keyinstance in depths and depths[keyinstance] == depth:
                    print results
                    return False
                if keyinstance not in depths or depths[keyinstance] > depth:
                    depths[keyinstance] = depth
                    content[keyinstance] = getattr(obj, valuename, None)
    return True
