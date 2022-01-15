from django.core.management.base import BaseCommand
from math_app.models import *
from user_app.models import *
import random

class Command( BaseCommand ):
    # начальное заполнение БД
    def handle(self, *args, **options):
        # уроки

        stud = MathUser.objects.all()
        task = Task.objects.all()

        # Каждому студенту назначается задача.  На которую он случайно отвечает
        for s in stud:
            if s.is_student:
                s_id = s.id
                for t in task:
                    t_id = t.id
                    Lesson.objects.create( student_id=s_id, task_id=t_id)