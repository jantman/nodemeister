"""
Classes, serializers, router registration for NodeMeister
ENC django-rest-framework API
"""

from rest_framework import viewsets, routers, serializers
from models import *


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('hostname',
                  'description',
                  'groups',
                  'excluded_groups',
                  'parameters',
                  'classes',
                  'excluded_params',
                  'excluded_classes',
                  'id'
                  )


class NodeViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    model = Node


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'description', 'groups', 'parents',
                  'parameters', 'classes', 'parameters', 'classes', 'id')


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    model = Group


class NodeClassViewSet(viewsets.ModelViewSet):
    model = NodeClass


class GroupClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupClass
        fields = ('group', 'classname', 'classparams', 'id')


class GroupClassViewSet(viewsets.ModelViewSet):
    serializer_class = GroupClassSerializer
    model = GroupClass


class NodeParamViewSet(viewsets.ModelViewSet):
    model = NodeParameter


class GroupParamViewSet(viewsets.ModelViewSet):
    model = GroupParameter


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'nodes', NodeViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'classes/nodes', NodeClassViewSet)
router.register(r'classes/groups', GroupClassViewSet)
router.register(r'parameters/nodes', NodeParamViewSet)
router.register(r'parameters/groups', GroupParamViewSet)
