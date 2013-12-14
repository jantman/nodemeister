# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'NodeParameter', fields ['node', 'key']
        db.create_unique(u'enc_nodeparameter', ['node_id', 'key'])

        # Adding unique constraint on 'ParamExclusion', fields ['node', 'exclusion']
        db.create_unique(u'enc_paramexclusion', ['node_id', 'exclusion'])

        # Adding unique constraint on 'GroupClass', fields ['classname', 'group']
        db.create_unique(u'enc_groupclass', ['classname', 'group_id'])

        # Adding unique constraint on 'Group', fields ['name']
        db.create_unique(u'enc_group', ['name'])

        # Adding unique constraint on 'Node', fields ['hostname']
        db.create_unique(u'enc_node', ['hostname'])

        # Adding unique constraint on 'ClassExclusion', fields ['node', 'exclusion']
        db.create_unique(u'enc_classexclusion', ['node_id', 'exclusion'])

        # Adding unique constraint on 'GroupParameter', fields ['group', 'key']
        db.create_unique(u'enc_groupparameter', ['group_id', 'key'])

        # Adding unique constraint on 'NodeClass', fields ['node', 'classname']
        db.create_unique(u'enc_nodeclass', ['node_id', 'classname'])


    def backwards(self, orm):
        # Removing unique constraint on 'NodeClass', fields ['node', 'classname']
        db.delete_unique(u'enc_nodeclass', ['node_id', 'classname'])

        # Removing unique constraint on 'GroupParameter', fields ['group', 'key']
        db.delete_unique(u'enc_groupparameter', ['group_id', 'key'])

        # Removing unique constraint on 'ClassExclusion', fields ['node', 'exclusion']
        db.delete_unique(u'enc_classexclusion', ['node_id', 'exclusion'])

        # Removing unique constraint on 'Node', fields ['hostname']
        db.delete_unique(u'enc_node', ['hostname'])

        # Removing unique constraint on 'Group', fields ['name']
        db.delete_unique(u'enc_group', ['name'])

        # Removing unique constraint on 'GroupClass', fields ['classname', 'group']
        db.delete_unique(u'enc_groupclass', ['classname', 'group_id'])

        # Removing unique constraint on 'ParamExclusion', fields ['node', 'exclusion']
        db.delete_unique(u'enc_paramexclusion', ['node_id', 'exclusion'])

        # Removing unique constraint on 'NodeParameter', fields ['node', 'key']
        db.delete_unique(u'enc_nodeparameter', ['node_id', 'key'])


    models = {
        u'enc.classexclusion': {
            'Meta': {'unique_together': "(('node', 'exclusion'),)", 'object_name': 'ClassExclusion'},
            'exclusion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'excluded_classes'", 'to': u"orm['enc.Node']"})
        },
        u'enc.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'children'", 'blank': 'True', 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'enc.groupclass': {
            'Meta': {'unique_together': "(('group', 'classname'),)", 'object_name': 'GroupClass'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'classparams': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'enc.groupparameter': {
            'Meta': {'unique_together': "(('group', 'key'),)", 'object_name': 'GroupParameter'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parameters'", 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'enc.node': {
            'Meta': {'object_name': 'Node'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'excluded_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'excluded_nodes'", 'blank': 'True', 'to': u"orm['enc.Group']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'nodes'", 'blank': 'True', 'to': u"orm['enc.Group']"}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'enc.nodeclass': {
            'Meta': {'unique_together': "(('node', 'classname'),)", 'object_name': 'NodeClass'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'classparams': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['enc.Node']"})
        },
        u'enc.nodeparameter': {
            'Meta': {'unique_together': "(('node', 'key'),)", 'object_name': 'NodeParameter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parameters'", 'to': u"orm['enc.Node']"}),
            'value': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'enc.paramexclusion': {
            'Meta': {'unique_together': "(('node', 'exclusion'),)", 'object_name': 'ParamExclusion'},
            'exclusion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'excluded_params'", 'to': u"orm['enc.Node']"})
        }
    }

    complete_apps = ['enc']