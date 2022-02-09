from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import  static
from math_app.api_views import *
# from user_app.api_views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register( 'task', TaskViewSet )
router.register( 'variant', VariantViewSet )
router.register( 'theme', ThemeViewSet )
router.register( 'level', LevelViewSet )
router.register( 'partition', PartitionViewSet )
router.register( 'lesson', LessonViewSet )
router.register( 'answer', AnswerViewSet )
# router.register( 'mathuser', MathUserViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', include( 'math_app.urls', namespace='mathapp' ) ),
    path( 'users/', include( 'user_app.urls', namespace='userapp' ) ),

    path( 'api/v0/', include( router.urls ) )
]
if settings.DEBUG:  # связь url хранения и путь поиска
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]