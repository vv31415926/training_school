from django.urls import path, include
from .views import *

app_name = 'math_app'

urlpatterns = [
    path( '', main_page,   name='index'  ),
    path('table_tasks/',         TasksPage.as_view(),  name='tasks_table'),

    path('task/<int:task_id>/',  ShowTask.as_view(),    name='task_one'),

    path('newtask/',             NewTask.as_view(),     name='task_new'),

    path('newversion/<int:task_id>/',  NewVersion.as_view(),  name='version_new'),

    path('version/<int:version_id>/', ShowVersion.as_view(), name='version_one'),

    path('lessons/<int:student_id>/',     UserLessons.as_view(),      name='user_lessons'),


    #path('usertasks/',         UserTasks.as_view(),  name='user_tasks'),
    #path('usertasks/',         user_tasks,  name='user_tasks'),
]
