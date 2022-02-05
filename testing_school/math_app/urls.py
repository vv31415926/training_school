from django.urls import path, include
from .views import *

app_name = 'math_app'

urlpatterns = [
    path( '',                           main_page,   name='index'  ),
    # Темы по разделам
    path( 'partition/',                  PartitionsPage.as_view(), name='partitions'),
    # Задачи темы
    path( 'tasks-theme/<int:theme_id>/', ShowTaskTheme.as_view(),    name='tasks_theme'),
    path( 'new-task/<int:theme_id>/',    NewTask.as_view(),     name='task_new'),
    # Варианты  задачи
    path( 'variants-task/<int:theme_id>/<int:task_id>/', VariantsTask.as_view(),     name='variants_task'),
    path( 'new-variant/<int:theme_id>/<int:task_id>/',  NewVariant.as_view(),     name='variant_new'),
    path( 'variant_assign/<int:theme_id>/<int:task_id>/<int:variant_id>/',   VariantAssign.as_view(), name='variant_assign' ),
    # ответы на вариант
    path( 'new-answer/<int:theme_id>/<int:task_id>/<int:variant_id>/',  NewAnswer.as_view(),  name='answer_new'),

    # Уроки студента - для учителя
    path( 'lessons-user/<int:mathuser_id>/', LessonsUser.as_view(), name='lessons_user'),
    # Уроки заданные для вошедшего студента
    path( 'assigned-lessons/<int:mathuser_id>/', AssignedLessons.as_view(), name='assigned_lessons'),


    path( 'create-lesson/<int:theme_id>/<int:task_id>/<int:variant_id>',   lessonVariantCreate.as_view(), name='create_lesson' ),









    #path('user-lessons/<int:student_id>/',     UserLessons.as_view(),      name='user_lessons'),

    # path('table_tasks/',         TasksPage.as_view(),  name='tasks_table'),
    #
    # path('task/<int:task_id>/',  ShowTask.as_view(),    name='task_one'),
    #
    # path('newx`/<int:task_id>/',  NewVersion.as_view(),  name='version_new'),
    #
    # path('version/<int:version_id>/', ShowVersion.as_view(), name='version_one'),
    #



    # path('theme/',              ThemesPage.as_view(), name='themes'),


]
