"""
Tests for Django Models
mainly just custom functions
"""

import pytest
import enc
import django


class TestENCModels():
    """
    Tests for ENC app models.

    @TODO - do I need to test things like ensuring these models stay unique or uniquetogether?
    """

    # mark everything in the class as requiring DB access, and unit tests requiring db
    pytestmark = [pytest.mark.django_db, pytest.mark.unitdb]

    #
    # enc.models.Group
    #

    def test_model_group_unicode(self):
        """
        Test ``enc.models.Group`` model __unicode__ method
        """
        g = enc.models.Group.objects.create(name='group1', description='groupOne')
        assert str(g) == "group1"

    def test_model_group_parents(self):
        """
        Test ``enc.models.Group`` parents
        """
        g = enc.models.Group.objects.create(name='group1', description='groupOne')
        g2 = enc.models.Group.objects.create(name='group2', description='groupTwo')
        g.parents.add(g2)
        g3 = enc.models.Group.objects.create(name='group3', description='groupThree')
        g.parents.add(g3)

        assert g.parents.count() == 2

    def test_model_group_unique_name(self):
        """
        Test ``enc.models.Group`` unique name
        """
        g = enc.models.Group.objects.create(name='group1', description='groupOne')

        # test unique name
        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.Group.objects.create(name='group1', description='groupOneAgain')
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_group_name_key"\nDETAIL:  Key (name)=(group1) already exists.\n'

    def test_model_group_blank_description(self):
        """
        Test ``enc.models.Group`` blank description
        """
        g = enc.models.Group.objects.create(name='group1')
        assert g.description == ""

    #
    # enc.models.Node
    #

    def test_model_node_unicode(self):
        """
        Test ``enc.models.Node`` model __unicode__ method
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        assert str(n) == "node1"

    def test_model_node_unique_name(self):
        """
        Test ``enc.models.Node`` unique name
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')

        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.Node.objects.create(hostname='node1', description='nodeOneAgain')
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_node_hostname_key"\nDETAIL:  Key (hostname)=(node1) already exists.\n'

    def test_model_node_blank_description(self):
        """
        Test ``enc.models.Node`` blank description
        """
        n = enc.models.Node.objects.create(hostname='node1')
        assert n.description == ""

    def test_model_node_groups(self):
        """
        Test ``enc.models.Node`` with multiple groups
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        g = enc.models.Group.objects.create(name='group1', description='groupOne')
        g2 = enc.models.Group.objects.create(name='group2', description='groupTwo')
        n.groups.add(g)
        n.groups.add(g2)
        assert n.groups.count() == 2

    def test_model_node_excluded_groups(self):
        """
        Test ``enc.models.Node`` excluded groups
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        g = enc.models.Group.objects.create(name='group1', description='groupOne')
        g2 = enc.models.Group.objects.create(name='group2', description='groupTwo')
        g3 = enc.models.Group.objects.create(name='group3', description='groupThree')
        g4 = enc.models.Group.objects.create(name='group4', description='groupFour')
        n.groups.add(g)
        n.groups.add(g2)
        n.excluded_groups.add(g3)
        n.excluded_groups.add(g4)
        assert n.groups.count() == 2
        assert n.excluded_groups.count() == 2

    #
    # enc.models.GroupClass
    #

    def test_model_groupclass_blank_params(self):
        """
        Test ``enc.models.GroupClass`` with blank classparams
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gc = enc.models.GroupClass.objects.create(group=g, classname="gclassname")
        assert gc.classparams == ""

    def test_model_groupclass_string_params(self):
        """
        Test ``enc.models.GroupClass`` with string classparams
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gc = enc.models.GroupClass.objects.create(group=g, classname="gclassname", classparams="foobar")
        assert gc.classparams == "foobar"

    def test_model_groupclass_int_params(self):
        """
        Test ``enc.models.GroupClass`` with int classparams
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gc = enc.models.GroupClass.objects.create(group=g, classname="gclassname", classparams=100)
        assert gc.classparams == 100

    def test_model_groupclass_json_params(self):
        """
        Test ``enc.models.GroupClass`` with json classparams
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gc = enc.models.GroupClass.objects.create(group=g, classname="gclassname", classparams="{'foo': 'bar', 'baz': 3}")
        assert gc.classparams == "{'foo': 'bar', 'baz': 3}"

    def test_model_groupclass_unique(self):
        """
        Test ``enc.models.GroupClass`` unique classname
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gc = enc.models.GroupClass.objects.create(group=g, classname="gclassname")

        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.GroupClass.objects.create(group=g, classname="gclassname")
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_groupclass_group_id_classname_key"\nDETAIL:  Key (group_id, classname)=(%d, gclassname) already exists.\n' % g.id

    def test_model_groupclass_unicode(self):
        """
        Test ``enc.models.GroupClass`` __unicode__ method
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gc = enc.models.GroupClass.objects.create(group=g, classname="gclassname")
        assert str(gc) == "group2->gclassname"

    #
    # NodeClass
    #

    # NodeClass - unicode
    # NodeClass - blank classname
    # NodeClass - duplicate classname
    # NodeClass - blank classparams
    # NodeClass - string classparams
    # NodeClass - int classparams
    # NodeClass - json classparams

    def test_model_nodeclass(self):
        """
        Test custom methods on the NodeClass model
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        nc = enc.models.NodeClass.objects.create(node=n, classname="nclassname")

        # test __unicode__ method
        assert str(nc) == "node1->nclassname"

        # test unique_together constraint
        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.NodeClass.objects.create(node=n, classname="nclassname")
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_nodeclass_node_id_classname_key"\nDETAIL:  Key (node_id, classname)=(%d, nclassname) already exists.\n' % n.id

    #
    # GroupParameter
    #

    # GroupParameter - unicode
    # GroupParameter - blank paramkey
    # GroupParameter - duplicate paramkey
    # GroupParameter - blank paramvalue
    # GroupParameter - string paramvalue
    # GroupParameter - int paramvalue
    # GroupParameter - json paramvalue

    def test_model_groupparameter(self):
        """
        Test custom methods on the GroupParameter model
        """
        g = enc.models.Group.objects.create(name='group2', description='groupTwo')
        gp = enc.models.GroupParameter.objects.create(group=g, paramkey='gpkey', paramvalue='foo')

        # test __unicode__ method
        assert str(gp) == "group2->gpkey"

        # test unique_together constraint
        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.GroupParameter.objects.create(group=g, paramkey='gpkey')
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_groupparameter_group_id_paramkey_key"\nDETAIL:  Key (group_id, paramkey)=(%d, gpkey) already exists.\n' % g.id

    #
    # NodeParameter
    #

    # NodeParameter - unicode
    # NodeParameter - blank paramkey
    # NodeParameter - duplicate paramkey
    # NodeParameter - blank paramvalue
    # NodeParameter - string paramvalue
    # NodeParameter - int paramvalue
    # NodeParameter - json paramvalue

    def test_model_nodeparameter(self):
        """
        Test custom methods on the NodeParameter model
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        np = enc.models.NodeParameter.objects.create(node=n, paramkey='npkey', paramvalue='foo')

        # test __unicode__ method
        assert str(np) == "node1->npkey"

        # test unique_together constraint
        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.NodeParameter.objects.create(node=n, paramkey='npkey')
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_nodeparameter_node_id_paramkey_key"\nDETAIL:  Key (node_id, paramkey)=(%d, npkey) already exists.\n' % n.id

    #
    # ParamExclusion
    #

    # ParamExclusion - unicode
    # ParamExclusion - blank exclusion
    # ParamExclusion - duplicate exclusion

    def test_model_paramexclusion(self):
        """
        Test custom methods on the ParamExclusion model
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        pe = enc.models.ParamExclusion.objects.create(node=n, exclusion='foobar')

        # test __unicode__ method
        assert str(pe) == "node1->foobar"

        # test unique_together constraint
        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.ParamExclusion.objects.create(node=n, exclusion='foobar')
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_paramexclusion_node_id_exclusion_key"\nDETAIL:  Key (node_id, exclusion)=(%d, foobar) already exists.\n' % n.id

    #
    # ClassExclusion
    #

    # ClassExclusion - unicode
    # ClassExclusion - blank exclusion
    # ClassExclusion - duplicate exclusion

    def test_model_classexclusion(self):
        """
        Test custom methods on the ClassExclusion model
        """
        n = enc.models.Node.objects.create(hostname='node1', description='nodeOne')
        ce = enc.models.ClassExclusion.objects.create(node=n, exclusion='foobaz')

        # test __unicode__ method
        assert str(ce) == "node1->foobaz"

        # test unique_together constraint
        with pytest.raises(django.db.IntegrityError) as excinfo:
            foo = enc.models.ClassExclusion.objects.create(node=n, exclusion='foobaz')
        assert excinfo.value.message == 'duplicate key value violates unique constraint "enc_classexclusion_node_id_exclusion_key"\nDETAIL:  Key (node_id, exclusion)=(%d, foobaz) already exists.\n' % n.id
