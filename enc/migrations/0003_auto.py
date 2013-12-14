# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field groups on 'Group'
        db.delete_table('enc_group_groups')

        # Adding M2M table for field parents on 'Group'
        db.create_table(u'enc_group_parents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_group', models.ForeignKey(orm[u'enc.group'], null=False)),
            ('to_group', models.ForeignKey(orm[u'enc.group'], null=False))
        ))
        db.create_unique(u'enc_group_parents', ['from_group_id', 'to_group_id'])


    def backwards(self, orm):
        # Adding M2M table for field groups on 'Group'
        db.create_table(u'enc_group_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_group', models.ForeignKey(orm[u'enc.group'], null=False)),
            ('to_group', models.ForeignKey(orm[u'enc.group'], null=False))
        ))
        db.create_unique(u'enc_group_groups', ['from_group_id', 'to_group_id'])

        # Removing M2M table for field parents on 'Group'
        db.delete_table('enc_group_parents')


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