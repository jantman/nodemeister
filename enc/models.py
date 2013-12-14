from django.db import models
import jsonfield
from fullhistory import register_model

class Group(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200,blank=True)
    parents = models.ManyToManyField("self", symmetrical=False,related_name='groups',blank=True)

class Node(models.Model):
    def __unicode__(self):
        return self.hostname
    hostname = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200,blank=True)
    excluded_groups = models.ManyToManyField(Group, related_name='excluded_nodes',blank=True)
    groups = models.ManyToManyField(Group, related_name='nodes',blank=True)
            
class GroupClass(models.Model):
    def __unicode__(self):
        return "%s->%s" % (self.group,self.classname)
    group = models.ForeignKey(Group,related_name='classes')
    classname = models.CharField(max_length=200)
    classparams = jsonfield.JSONField(blank=True)
    class Meta:
	unique_together = ("group","classname")

class NodeClass(models.Model):
    def __unicode__(self):
        return "%s->%s" % (self.node,self.classname)
    node = models.ForeignKey(Node, related_name='classes')
    classname = models.CharField(max_length=200)
    classparams = jsonfield.JSONField(blank=True)
    class Meta:
	unique_together = ("node","classname")

class GroupParameter(models.Model):
    def __unicode__(self):
        return "%s->%s" % (self.group,self.paramkey)
    group = models.ForeignKey(Group, related_name='parameters')
    paramkey = models.CharField(max_length=200)
    paramvalue = jsonfield.JSONField()
    class Meta:
	unique_together = ("group","paramkey")
    
class NodeParameter(models.Model):
    def __unicode__(self):
        return "%s->%s" % (self.node,self.paramkey)
    node = models.ForeignKey(Node, related_name='parameters')
    paramkey = models.CharField(max_length=200)
    paramvalue = jsonfield.JSONField()
    class Meta:
	unique_together = ("node","paramkey")

class ParamExclusion(models.Model):
    def __unicode__(self):
        return "%s->%s" % (self.node,self.exclusion)
    node = models.ForeignKey(Node, related_name='excluded_params')
    exclusion = models.CharField(max_length=200)
    class Meta:
	unique_together = ("node","exclusion")

class ClassExclusion(models.Model):
    def __unicode__(self):
        return "%s->%s" % (self.node,self.exclusion)
    node = models.ForeignKey(Node, related_name='excluded_classes')
    exclusion = models.CharField(max_length=200)
    class Meta:
	unique_together = ("node","exclusion")
	
register_model(Group)
register_model(Node)
register_model(NodeClass)
register_model(NodeParameter)

	