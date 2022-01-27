from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property


class StudentManager( models.Manager ):
    def get_queryset(self):
        obj = super().get_queryset()
        return obj.filter( is_student = True )

class IsStudentMixin(models.Model):
    objects = models.Manager()
    student_objects = StudentManager()
    is_student = models.BooleanField(default = True)
    class Meta:
        abstract = True

class MathUser(  IsStudentMixin, AbstractUser):
    email =         models.EmailField( unique=True, verbose_name='Почта')
    num_class =     models.IntegerField( blank=True, null=True, verbose_name='Класс' )
    letter_class =  models.CharField( max_length=1, blank=True, null=True,  verbose_name='литера класса')
    #is_student =    models.BooleanField(  default=True )
    def __str__(self):
        return f'{self.last_name} {self.first_name}, {self.num_class}{self.letter_class}'

    # def get_absolute_url(self):
    #     return reverse( 'userapp:user_one',  kwargs={'user_id':self.pk} )
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']
    def get_count_lessons(self):
        #return self.lesson_set.select_related('mathuser').all()   #.count()
        return self.lesson_set.all()

