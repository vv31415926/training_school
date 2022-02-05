from .models import Task, Variant
from .serializer  import TaskSerializer, VariantSerializer
from rest_framework import viewsets

class TaskViewSet( viewsets.ModelViewSet ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class VariantViewSet( viewsets.ModelViewSet ):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer