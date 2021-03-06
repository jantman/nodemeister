"""
NodeMeister ENC -
methods to aid in collection of resources
"""


def getExclusions(node):
    """
    Get excluded groups, classes, params for a node

    :param node: the node to get exclusions for
    :type node: Node
    :returns:  tuple: (list of excluded group names, list of excluded class names,
    list of excluded param names)
    """
    excluded_groups = []
    excluded_params = []
    excluded_classes = []
    for group_exclusion in node.excluded_groups.all():
        excluded_groups.append(group_exclusion.group.name)
    for class_exclusion in node.excluded_classes.all():
        excluded_classes.append(class_exclusion.exclusion)
    for param_exclusion in node.excluded_params.all():
        excluded_params.append(param_exclusion.exclusion)
    return (excluded_groups, excluded_classes, excluded_params)


def walkTree(groups, excluded_groups=[],
             excluded_classes=[], excluded_params=[]):
    """

    """
    classes = {}
    params = {}
    for groupmember in groups.all():
        if groupmember.group.name not in excluded_groups:
            if groupmember.group.groups.all() is not []:
                more_groups = groupmember.group.groups.all()
                (newclasses, newparams) = walkTree(more_groups,
                                                   excluded_groups,
                                                   excluded_classes
                                                   )
                classes.update(newclasses)
                params.update(newparams)
                for groupclass in groupmember.group.classes.all():
                    if groupclass.classname not in excluded_classes:
                        if not groupclass.classparams:
                            classes[groupclass.classname] = None
                        else:
                            classes[groupclass.classname] = json.loads(groupclass.classparams)
                for groupparams in groupmember.group.parameters.all():
                    if groupparams.key not in excluded_params:
                        if not groupparams.value:
                            params[groupparams.key] = None
                        else:
                            params[groupparams.key] = json.loads(groupparams.value)
    return (classes, params)
