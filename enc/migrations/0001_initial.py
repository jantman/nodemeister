# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'enc_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'enc', ['Group'])

        # Adding M2M table for field groups on 'Group'
        db.create_table(u'enc_group_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_group', models.ForeignKey(orm[u'enc.group'], null=False)),
            ('to_group', models.ForeignKey(orm[u'enc.group'], null=False))
        ))
        db.create_unique(u'enc_group_groups', ['from_group_id', 'to_group_id'])

        # Adding model 'Node'
        db.create_table(u'enc_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'enc', ['Node'])

        # Adding M2M table for field excluded_groups on 'Node'
        db.create_table(u'enc_node_excluded_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('node', models.ForeignKey(orm[u'enc.node'], null=False)),
            ('group', models.ForeignKey(orm[u'enc.group'], null=False))
        ))
        db.create_unique(u'enc_node_excluded_groups', ['node_id', 'group_id'])

        # Adding M2M table for field groups on 'Node'
        db.create_table(u'enc_node_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('node', models.ForeignKey(orm[u'enc.node'], null=False)),
            ('group', models.ForeignKey(orm[u'enc.group'], null=False))
        ))
        db.create_unique(u'enc_node_groups', ['node_id', 'group_id'])

        # Adding model 'GroupClass'
        db.create_table(u'enc_groupclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='classes', to=orm['enc.Group'])),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('classparams', self.gf('jsonfield.fields.JSONField')(default={}, blank=True)),
        ))
        db.send_create_signal(u'enc', ['GroupClass'])

        # Adding model 'NodeClass'
        db.create_table(u'enc_nodeclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='classes', to=orm['enc.Node'])),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('classparams', self.gf('jsonfield.fields.JSONField')(default={}, blank=True)),
        ))
        db.send_create_signal(u'enc', ['NodeClass'])

        # Adding model 'GroupParameter'
        db.create_table(u'enc_groupparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parameters', to=orm['enc.Group'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'enc', ['GroupParameter'])

        # Adding model 'NodeParameter'
        db.create_table(u'enc_nodeparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parameters', to=orm['enc.Node'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'enc', ['NodeParameter'])

        # Adding model 'ParamExclusion'
        db.create_table(u'enc_paramexclusion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='excluded_params', to=orm['enc.Node'])),
            ('exclusion', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'enc', ['ParamExclusion'])

        # Adding model 'ClassExclusion'
        db.create_table(u'enc_classexclusion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='excluded_classes', to=orm['enc.Node'])),
            ('exclusion', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'enc', ['ClassExclusion'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'enc_group')

        # Removing M2M table for field groups on 'Group'
        db.delete_table('enc_group_groups')

        # Deleting model 'Node'
        db.delete_table(u'enc_node')

        # Removing M2M table for field excluded_groups on 'Node'
        db.delete_table('enc_node_excluded_groups')

        # Removing M2M table for field groups on 'Node'
        db.delete_table('enc_node_groups')

        # Deleting model 'GroupClass'
        db.delete_table(u'enc_groupclass')

        # Deleting model 'NodeClass'
        db.delete_table(u'enc_nodeclass')

        # Deleting model 'GroupParameter'
        db.delete_table(u'enc_groupparameter')

        # Deleting model 'NodeParameter'
        db.delete_table(u'enc_nodeparameter')

        # Deleting model 'ParamExclusion'
        db.delete_table(u'enc_paramexclusion')

        # Deleting model 'ClassExclusion'
        db.delete_table(u'enc_classexclusion')


    models = {
        u'enc.classexclusion': {
            'Meta': {'object_name': 'ClassExclusion'},
            'exclusion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'excluded_classes'", 'to': u"orm['enc.Node']"})
        },
        u'enc.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'children'", 'blank': 'True', 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'enc.groupclass': {
            'Meta': {'object_name': 'GroupClass'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'classparams': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['enc.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'enc.groupparameter': {
            'Meta': {'object_name': 'GroupParameter'},
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
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'enc.nodeclass': {
            'Meta': {'object_name': 'NodeClass'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'classparams': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['enc.Node']"})
        },
        u'enc.nodeparameter': {
            'Meta': {'object_name': 'NodeParameter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parameters'", 'to': u"orm['enc.Node']"}),
            'value': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'enc.paramexclusion': {
            'Meta': {'object_name': 'ParamExclusion'},
            'exclusion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'excluded_params'", 'to': u"orm['enc.Node']"})
        }
    }

    complete_apps = ['enc']