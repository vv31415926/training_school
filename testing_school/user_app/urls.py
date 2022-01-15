from django.urls import path, include
from .views import *
from django.contrib.auth.views import   LogoutView

app_name = 'user_app'

urlpatterns = [
    path( 'login/',  UserLoginView.as_view(),  name='login' ),
    path( 'logout/', UserLogoutView.as_view(), name='logout' ),
    path( 'register/', UserRegisterView.as_view(), name='register' ),

    path( 'table_user/',   UsersTable.as_view(), name='users_table' ),

    path( 'select_user/',   SelectUser.as_view(), name='select_user' ),

    path( 'test/',   test_view, name='test' ),

    #path('student/<int:user_id>/',   ShowUser.as_view(), name='user_one'),
]
