from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class MathUser( AbstractUser):
    email =         models.EmailField( unique=True, verbose_name='Почта')
    num_class =     models.IntegerField( blank=True, null=True, verbose_name='Класс' )
    letter_class =  models.CharField( max_length=1, blank=True, null=True,  verbose_name='литера класса')
    is_student =    models.BooleanField(  default=True )
    def __str__(self):
        return f'{self.last_name} {self.first_name}, {self.num_class}{self.letter_class}'

    # def get_absolute_url(self):
    #     return reverse( 'userapp:user_one',  kwargs={'user_id':self.pk} )
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']
    def get_count_lessons(self):
        #print( '>>>>',  self.lesson_set.all().count()   )
        return self.lesson_set.all().count()

