from django.db import models
from django.views.generic import *
from django.urls import reverse

#import user_app
from user_app.models import MathUser
# import user_app.models

class Partition( models.Model ):
    '''
    Разделы задач
    '''
    num = models.IntegerField()
    name = models.CharField( max_length=32 )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['num']
    def get_theme_partition(self):
        theme = Theme.objects.filter( partition_id = self.pk ).order_by( 'num' )
        return theme

class Theme( models.Model ):
    '''
    темы задач по разделам
    '''
    num = models.IntegerField()
    name = models.CharField( max_length=512 )
    partition = models.ForeignKey( 'Partition', on_delete=models.SET_NULL , null=True )

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['name']
    def __str__(self):
        return f'{self.num}-{self.name}'

class Task( models.Model ):
    '''
    Наименования задач (не условие, а предмет задачи)
    '''
    num = models.IntegerField( default=0 , verbose_name='Номер')
    name = models.CharField( max_length=100, verbose_name='Задача' )
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    numclass = models.IntegerField(blank=True,default=0, verbose_name='класс')
    set_time = models.IntegerField( default=0 , verbose_name='Время на выполнение')
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тема')
    def __str__(self):
        return f'{self.num}: {self.name}'
    # def get_absolute_url(self):
    #     return reverse( 'mathapp:task_theme',  kwargs={'theme_id':self.pk} )
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['num']
    def get_count_variant(self):
        return self.variant_set.all().count()


class Variant( models.Model ):
    '''
        Вариант условия задачи
        '''
    num = models.IntegerField( default=0 , null=True, blank=True, verbose_name='Номер')
    question = models.TextField( blank=True, verbose_name='Условие' )
    img = models.ImageField( upload_to='task', blank=True, null=True, verbose_name='Чертеж')
    is_close = models.BooleanField( default=False, verbose_name='Закрыто' )
    is_select = models.BooleanField( default=True, verbose_name='Выбор ответа' )
    task = models.ForeignKey( 'Task', on_delete=models.CASCADE, null=True, verbose_name= 'Задача' )
    level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True, verbose_name='Уровень')
    def __str__(self):
        if len( self.question ) > 30:
            s = str( self.question )[0:30]
            return f'{s}...'
        else:
            return f'{self.num}. {self.question }'
    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'
        ordering = ['level_id']
    def get_count_lessons(self):
        return self.lesson_set.all().count()
    def is_image(self):
        return bool( self.img )
    def get_variant_answers(self):
        obj = self.answer_set.all()
        return obj

class Answer(models.Model):
    '''
    ответы на варианты задач
    '''
    npp = models.IntegerField(default=0, verbose_name= 'N п/п' )
    name = models.CharField(max_length=100, verbose_name= 'Ответ' )
    correct = models.BooleanField(default=False, verbose_name= 'Результат проверки' )
    is_close = models.BooleanField(default=False, verbose_name= 'Закрыто' )
    variant = models.ForeignKey('Variant', on_delete=models.CASCADE, null=True, verbose_name= 'Условие варианта задачи' )
    def __str__(self):
        return f'{self.answer}'
    # def get_absolute_url(self):
    #     return reverse( 'mathapp:version_one',  kwargs={'version_id':self.pk} )
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    # def get_task_id(self):
    #     v = self.variant.task_id
    #     return  v


class Lesson( models.Model ):
    num = models.IntegerField(default=0, verbose_name='Номер')
    status = models.CharField(max_length=13, default='не проверено', verbose_name= 'Статус')
    begin_answer = models.DateTimeField(null=True, blank=True, verbose_name= 'Дата ответа')
    date_check = models.DateTimeField(null=True, blank=True, verbose_name= 'Дата проверки')
    end_answer = models.DateTimeField(null=True, blank=True, verbose_name= 'Конец ответа')
    create_lesson = models.DateTimeField( auto_now_add=True, verbose_name= 'Создание урока')

    answer = models.ForeignKey(  'Answer', on_delete=models.CASCADE , null=True, verbose_name= 'Ответ')
    variant = models.ForeignKey(  'Variant', on_delete=models.CASCADE , null=True, verbose_name= 'Вариант задачи')     #? , null=True
    mathuser = models.ForeignKey( 'user_app.MathUser',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  #verbose_name='Студенты',
                                  limit_choices_to={'is_student': True}  )
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
    # def __str__(self):
    #     s = str(self.task)[0:30]
    #     return f' ответ {self.answer}, оценка "{self.correctly}", задание "{s}..."'
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

    def get_count_variant(self):
        return self.variant_set.all().count()





