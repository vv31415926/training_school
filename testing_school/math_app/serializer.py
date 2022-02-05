from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import Task, Variant

class TaskSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Task
        exclude = ['theme']

class VariantSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Variant
        exclude = ['task', 'level']