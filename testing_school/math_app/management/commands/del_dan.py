from django.core.management.base import BaseCommand
from math_app.models import *
from user_app.models import *

class Command( BaseCommand ):
    def handle(self, *args, **options):
        stud = MathUser.objects.all()
        stud.delete()

        tsk = Task.objects.all()  # A5 engl
        tsk.delete()

