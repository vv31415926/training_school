from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', include( 'math_app.urls', namespace='mathapp' ) ),
    path( 'users/', include( 'user_app.urls', namespace='userapp' ) ),
]
if settings.DEBUG:  # связь url хранения и путь поиска
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )