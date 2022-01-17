from django.db import models
from django.views.generic import *
from django.urls import reverse

#import user_app
from user_app.models import MathUser
# import user_app.models


# class Students( models.Model ):
#     students = models.ForeignKey(  'user_app.MathUser',  on_delete=models.CASCADE, verbose_name= 'Студенты' )

# Список задач для тестов
class Task( models.Model ):
    numtask = models.IntegerField( default=0 , verbose_name='Номер')
    variant = models.IntegerField( default=0, verbose_name= 'Вариант')
    question = models.TextField(blank=True, verbose_name='Условие')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    img = models.ImageField( upload_to='task', blank=True, null=True, verbose_name= 'Чертеж')
    numclass = models.IntegerField(blank=True,default=0, verbose_name='класс')
    theme = models.ForeignKey( 'Theme', on_delete=models.SET_NULL, null=True, blank=True, verbose_name= 'Тема')
    level = models.ForeignKey( 'Level', on_delete=models.SET_NULL, null=True, blank=True, verbose_name= 'Уровень')
    def __str__(self):
        return f'{self.numtask}: {self.question}'
    def get_absolute_url(self):
        return reverse( 'mathapp:task_one',  kwargs={'task_id':self.pk} )
    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['theme_id','numtask','variant']
    def get_count_lessons(self):
        return self.lesson_set.all().count()
    def is_image(self):
        return bool( self.img )

class Partition( models.Model ):
    num = models.IntegerField()
    name = models.CharField( max_length=32 )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

class Version(models.Model):
    npp = models.IntegerField(default=0, verbose_name= 'N п/п' )
    answer = models.CharField(max_length=100, verbose_name= 'Ответ' )
    correct = models.BooleanField(default=False, verbose_name= 'Правильно' )
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, verbose_name= 'Задача' )

    def __str__(self):
        return f'{self.answer}'

    def get_absolute_url(self):
        return reverse( 'mathapp:version_one',  kwargs={'version_id':self.pk} )

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

class Lesson( models.Model ):
    answer = models.IntegerField(                default=0 )
    correctly = models.CharField( max_length=13, default='не проверено')
    begin_lesson = models.DateTimeField( auto_now_add=True)
    date_answer = models.DateTimeField(  null=True, blank=True  )
    date_check = models.DateTimeField(  null = True, blank = True  )

    task = models.ForeignKey(  'Task', on_delete=models.CASCADE , null=True)     #? , null=True
    student = models.ForeignKey( MathUser, on_delete=models.CASCADE, null=True, verbose_name= 'Студенты' )
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
    def __str__(self):
        s = str(self.task)[0:30]
        return f' ответ {self.answer}, оценка "{self.correctly}", задание "{s}..."'
    def get_absolute_url(self):
        return reverse( 'mathapp:lesson_one',  kwargs={'lesson_id':self.pk} )



class Level( models.Model ):
    num = models.IntegerField()
    name = models.CharField( max_length=16 )
    def __str__(self):
        return f'{self.num}-{self.name}'
    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'
        ordering = ['num']

    def get_count_tasks(self):
        #print( '>>>>', self.task_set.all().count()   )
        return self.task_set.all().count()

class Theme( models.Model ):
    num = models.IntegerField()
    name = models.CharField( max_length=512 )
    partition = models.ForeignKey( 'Partition', on_delete=models.SET_NULL , null=True )

    def __str__(self):
        return f'{self.num}-{self.name}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['name']