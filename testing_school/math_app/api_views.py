from .models import *
from .serializer  import *
from rest_framework import viewsets
from .permissions import ReadOnly
from rest_framework.permissions import  IsAdminUser, IsAuthenticated

class TaskViewSet( viewsets.ModelViewSet ):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class VariantViewSet( viewsets.ModelViewSet ):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

class ThemeViewSet( viewsets.ModelViewSet ):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class LevelViewSet( viewsets.ModelViewSet ):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class AnswerViewSet( viewsets.ModelViewSet ):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class PartitionViewSet( viewsets.ModelViewSet ):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Partition.objects.all()
    serializer_class = PartitionSerializer

class LessonViewSet( viewsets.ModelViewSet ):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer