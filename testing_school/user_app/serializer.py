from rest_framework import routers, serializers, viewsets
from .models import *

class MathUserSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = MathUser
        fields =  ['first_name']   #'__all__'