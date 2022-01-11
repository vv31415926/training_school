from django import template
from math_app.models import *
from user_app.models import *

register = template.Library()

@register.simple_tag()
def set_task_lesson():
    #print( '>>>>>>>>>>>>>>>>>>>>>>>>>> set_task_lesson()'  )
    stud = MathUser.objects.all()
    tsk = Task.objects.all()
    return  'Назначить...'