from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import *

class TaskSerializer( serializers.HyperlinkedModelSerializer ):
    #theme = serializers.StringRelatedField()
    #theme = serializers.PrimaryKeyRelatedField( many=True, read_only=True )
    class Meta:
        model = Task
        fields = '__all__'

class VariantSerializer( serializers.HyperlinkedModelSerializer ):
    # task = serializers.StringRelatedField()
    # level = serializers.StringRelatedField()
    class Meta:
        model = Variant
        exclude = ['img']

class ThemeSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Theme
        fields = '__all__'
        #exclude = ['partition']

class LevelSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Level
        fields = '__all__'

class PartitionSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Partition
        fields = '__all__'

class LessonSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Lesson
        #fields = '__all__'
        exclude = ['mathuser']

class AnswerSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Answer
        fields = '__all__'
