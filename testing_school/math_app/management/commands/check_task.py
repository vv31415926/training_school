from django.core.management.base import BaseCommand
from math_app.models import *

class Command( BaseCommand ):
    def handle(self, *args, **options):
        lesson = Lesson.objects.filter( correctly='не проверено' )
        for les in lesson:
            vers = Version.objects.filter(  task=les.task_id )
            #print( les.answer, les.correctly, les.task )
            for v in vers:
                #print(v.npp, v.variant, v.correct)
                if les.answer == v.npp:
                    if v.correct:
                        les.correctly = 'верно'
                    else:
                        les.correctly = 'ошибка'
                    les.save()
