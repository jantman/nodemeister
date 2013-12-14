from enc.models import *
import yaml, json

nodename = "djaapafes30.ddtc.cmgdigital.com"

node = Node.objects.filter(name=nodename)[0]
groups = node.groups

def getExclusions(node):
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
  

def walkTree(groups,excluded_groups=[],excluded_classes=[],excluded_params=[]):
    classes = {}
    params = {}
    for groupmember in groups.all():
	if groupmember.group.name not in excluded_groups:
	    if groupmember.group.groups.all() is not []:
	        more_groups = groupmember.group.groups.all()
		(newclasses, newparams) =  walkTree(more_groups,excluded_groups,excluded_classes)
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
    

node = Node.objects.filter(name=nodename)[0]
groups = node.groups

(classlist, params) = walkTree(groups)
enc_output = {"classes":classlist, "parameters":params}
print "djaapafes30.ddtc.cmgdigital.com -> Group Apache -> class httpd"
print "                                -> Group FEs    -> class sudo"
print "                                                -> class solr({'blah': ['blah', 'blah', 'blah']})"
print "                                                -> param  some_data {'this':['is','data']}"
print "                                                -> param  some_other_data {'that':['was','data']}"
print ""
print "Full YAML:"
print yaml.safe_dump(enc_output, default_flow_style=False)

(excluded_groups, excluded_classes, excluded_params) = getExclusions(node)
(classlist, params) = walkTree(groups,excluded_groups,excluded_classes,excluded_params)
enc_output = {"classes":classlist, "parameters":params}

print "Excluded groups: %s" % excluded_groups
print "Excluded classes: %s" % excluded_classes
print "Excluded params: %s" % excluded_params
print ""
print "Excluded YAML:"
print yaml.safe_dump(enc_output, default_flow_style=False)