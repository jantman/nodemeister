# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'GroupParameter', fields ['group', 'key']
        db.delete_unique(u'enc_groupparameter', ['group_id', 'key'])

        # Removing unique constraint on 'NodeParameter', fields ['node', 'key']
        db.delete_unique(u'enc_nodeparameter', ['node_id', 'key'])

        # Deleting field 'NodeParameter.value'
        db.delete_column(u'enc_nodeparameter', 'value')

        # Deleting field 'NodeParameter.key'
        db.delete_column(u'enc_nodeparameter', 'key')

        # Adding field 'NodeParameter.paramkey'
        db.add_column(u'enc_nodeparameter', 'paramkey',
                      self.gf('django.db.models.fields.CharField')(default='{}', max_length=200),
                      keep_default=False)

        # Adding field 'NodeParameter.paramvalue'
        db.add_column(u'enc_nodeparameter', 'paramvalue',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding unique constraint on 'NodeParameter', fields ['node', 'paramkey']
        db.create_unique(u'enc_nodeparameter', ['node_id', 'paramkey'])

        # Deleting field 'GroupParameter.value'
        db.delete_column(u'enc_groupparameter', 'value')

        # Deleting field 'GroupParameter.key'
        db.delete_column(u'enc_groupparameter', 'key')

        # Adding field 'GroupParameter.paramkey'
        db.add_column(u'enc_groupparameter', 'paramkey',
                      self.gf('django.db.models.fields.CharField')(default='{}', max_length=200),
                      keep_default=False)

        # Adding field 'GroupParameter.paramvalue'
        db.add_column(u'enc_groupparameter', 'paramvalue',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding unique constraint on 'GroupParameter', fields ['paramkey', 'group']
        db.create_unique(u'enc_groupparameter', ['paramkey', 'group_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'GroupParameter', fields ['paramkey', 'group']
        db.delete_unique(u'enc_groupparameter', ['paramkey', 'group_id'])

        # Removing unique constraint on 'NodeParameter', fields ['node', 'paramkey']
        db.delete_unique(u'enc_nodeparameter', ['node_id', 'paramkey'])

        # Adding field 'NodeParameter.value'
        db.add_column(u'enc_nodeparameter', 'value',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'NodeParameter.key'
        db.add_column(u'enc_nodeparameter', 'key',
                      self.gf('django.db.models.fields.CharField')(default='{}', max_length=200),
                      keep_default=False)

        # Deleting field 'NodeParameter.paramkey'
        db.delete_column(u'enc_nodeparameter', 'paramkey')

        # Deleting field 'NodeParameter.paramvalue'
        db.delete_column(u'enc_nodeparameter', 'paramvalue')

        # Adding unique constraint on 'NodeParameter', fields ['node', 'key']
        db.create_unique(u'enc_nodeparameter', ['node_id', 'key'])

        # Adding field 'GroupParameter.value'
        db.add_column(u'enc_groupparameter', 'value',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'GroupParameter.key'
        db.add_column(u'enc_groupparameter', 'key',
                      self.gf('django.db.models.fields.CharField')(default='{}', max_length=200),
                      keep_default=False)

        # Deleting field 'GroupParameter.paramkey'
        db.delete_column(u'enc_groupparameter', 'paramkey')

        # Deleting field 'GroupParameter.paramvalue'
        db.delete_column(u'enc_groupparameter', 'paramvalue')

        # Adding unique constraint on 'GroupParameter', fields ['group', 'key']
        db.create_unique(u'enc_groupparameter', ['group_id', 'key'])


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'groups'", 'blank': 'True', 'to': u"orm['enc.Group']"})
        },
        u'enc.groupclass': {
            'Meta': {'unique_together': "(('group', 'classname'),)", 'object_name': 'GroupClass'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'classparams': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'enc.groupparameter': {
            'Meta': {'unique_together': "(('group', 'paramkey'),)", 'object_name': 'GroupParameter'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parameters'", 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paramkey': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paramvalue': ('jsonfield.fields.JSONField', [], {'default': '{}'})
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
            'Meta': {'unique_together': "(('node', 'paramkey'),)", 'object_name': 'NodeParameter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parameters'", 'to': u"orm['enc.Node']"}),
            'paramkey': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paramvalue': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'enc.paramexclusion': {
            'Meta': {'unique_together': "(('node', 'exclusion'),)", 'object_name': 'ParamExclusion'},
            'exclusion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'excluded_params'", 'to': u"orm['enc.Node']"})
        }
    }

    complete_apps = ['enc']