from django.urls import path, include
from .views import *
from django.contrib.auth.views import   LogoutView

app_name = 'user_app'

urlpatterns = [
    path( 'login/',  UserLoginView.as_view(),  name='login' ),
    path( 'logout/', UserLogoutView.as_view(), name='logout' ),
    path( 'register/', UserRegisterView.as_view(), name='register' ),

    path( 'table-user/',   StudentTable.as_view(), name='users_table' ),

    path( 'profile/<int:pk>/',  UserProfileView.as_view() , name='user_profile' ),
    path( 'update-token/', update_token, name='update_token' ),

    #path( 'test/',   test_view, name='test' ),

    # path( 'select_user/',   SelectUser.as_view(), name='select_user' ),
    # path( 'create-lesson/<int:variant_id>',   lessonVariantCreate.as_view(), name='create_lesson' ),
    #path('student/<int:user_id>/',   ShowUser.as_view(), name='user_one'),
]
