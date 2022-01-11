# Импортируемые данные
from django.contrib.auth.models import User
from django.utils.text import slugify

lst_partition=[
    {'num':1,'name':'Вычисления, преобразования'},
    {'num':2,'name':'Уравнения, неравенства'},
    {'num':3,'name':'Функции'},
    {'num':4,'name':'Геометрические фигуры, координаты, вектора'},
    {'num':5,'name':'Математические модели'},
    {'num':6,'name':'Применение'}
]

lst_theme=[
    {'partition_id':1, 'num':1, 'name':'Арифметические действия (устно, писменно), корень, степень, логарифм'},
    {'partition_id':2, 'num':1, 'name':'Решение уравнений, их систем'},
    {'partition_id':3, 'num':1, 'name':'Определять значение функции, по графику определять поведение и свойство функции'},
    {'partition_id':4, 'num':1, 'name':'Раходить геометрические величины (длинна, угол, площадь)'},
    {'partition_id':5, 'num':1, 'name':'Уравнения и неравенства по условию'},
    {'partition_id':6, 'num':1, 'name':'Анализ числовых данных, статистики, практические расчеты по формулам'}
]

lst_level=[
    {'num':1, 'name':'Простой'},
    {'num':2, 'name':'Средний'},
    {'num':3, 'name':'Сложный'},
    {'num':4, 'name':'Супер'}
]

lst_student = [
{'username':'vorob',        'last_name':'Воробьев', 'first_name':'Миша','email':'a1@mail.ru','class':'10','ch':'А'},
{'username':'scheg',        'last_name':'Щеглов',   'first_name':'Паша','email':'a2@mail.ru','class':'10','ch':'Б'},
{'username':'sinitchin',    'last_name':'Синицин',  'first_name':'Саша','email':'a3@mail.ru','class':'10','ch':'В'},
{'username':'sokolov',      'last_name':'Соколов',  'first_name':'Петя','email':'a4@mail.ru','class':'10','ch':'Г'},
{'username':'orlov',        'last_name':'Орлов',    'first_name':'Сергей','email':'a5@mail.ru','class':'10','ch':'А'},
{'username':'tchaplin',     'last_name':'Цаплин',   'first_name':'Виталий','email':'a6@mail.ru','class':'10','ch':'Б'},
{'username':'snigirev',     'last_name':'Снигирев', 'first_name':'Алексей','email':'a7@mail.ru','class':'10','ch':'В'},
{'username':'kukuschkin',   'last_name':'Кукушкин', 'first_name':'Федор','email':'a8@mail.ru','class':'10','ch':'Г'},
{'username':'suvuskin',     'last_name':'Савушкин', 'first_name':'Ераклий','email':'a9@mail.ru','class':'10','ch':'А'},
{'username':'kuropatkin',   'last_name':'Куропаткин','first_name':'Моисей','email':'a0@mail.ru','class':'10','ch':'Б'}
]
# A5 engl
lst_task=[
{'question':'Функция y=f(x)  задана своим графиком. Укажите в какой точке графика касательная к нему параллельна оси абсцисс.',
            'numtask':1,
            'variant':3,
            'level_id':2,
            'theme_id':3,
            'version': [{'variant':'(-3;-2)',   'correct':'0','npp':'1'},
                        {'variant':'(4;-2)',    'correct':'0','npp':'2'},
                        {'variant':'(3;1)',     'correct':'1','npp':'3'},
                        {'variant':'(-1;-3)',   'correct':'0','npp':'4'} ]},

{'question':'На рисунке изображен график производной некоторой функции. Укажите промежуток, на котором функция возрастает',
            'numtask':'1',
            'variant':'4',
            'level_id':2,
            'theme_id':3,
            'version': [{'variant':'(-3;1)',        'correct':'0','npp':'1'},
                        {'variant':'(-2;2)',        'correct':'0','npp':'2'},
                        {'variant':'(-&infin;;-1)', 'correct':'1','npp':'3'},
                        {'variant':'[0;10)',        'correct':'0','npp':'4'} ]},

{'question':'Точка движктся по закону S(t)=t^3-2*t^2. ' \
            'Выберите какой из формул задается скорость движения этой точки в момент времени t.',
            'numtask':'3',
            'variant':'3',
            'level_id':2,
            'theme_id':3,
            'version': [{'variant':'3*t^2-2','correct':'0','npp':'1'},
                        {'variant':'t^2-4*t','correct':'0','npp':'2'},
                        {'variant':'t^4/4-2*t^3/3','correct':'0','npp':'3'},
                        {'variant':'3*t^2-4*T','correct':'1','npp':'4'} ]},
{'question':'Зависимость температуры T тела от времени задана уравнением' \
            'T=1/2*T^2-2*t+5. С какой скоростью нагревается это тело в момент времени t=5с ?',
            'numtask':'4',
            'variant':'3',
            'level_id':2,
            'theme_id':3,
            'version': [{'variant':'3','correct':'1','npp':'1'},
                        {'variant':'-8','correct':'0','npp':'2'},
                        {'variant':'7,5','correct':'0','npp':'3'},
                        {'variant':'7','correct':'0','npp':'4'} ]},
{'question':'При движении тела по прямой расстояние S(t) в метрахот начальной точки M ' \
            'изменяется по закону S(t)=3*t^3+2*t^2+4*t+5 (t-время в секундах). Через сколько секунд ' \
            'после начала движения мгновенное  ускорение тела будет равно 58 м/с^2 ?',
            'numtask':'5',
            'variant':'3',
            'level_id':2,
            'theme_id':3,
            'version': [{'variant':'5c','correct':'0','npp':'1'},
                        {'variant':'3c','correct':'1','npp':'2'},
                        {'variant':'2c','correct':'0','npp':'3'},
                        {'variant':'0','correct':'0','npp':'4'} ]}
]
# Импорт:
from django.core.management.base import BaseCommand
from math_app.models import *
from user_app.models import *

class Command( BaseCommand ):
    # начальное заполнение БД
    def handle(self, *args, **options):

        part = Partition.objects.all()
        if len(part) == 0:  # база пуста
            for s in lst_partition:
                s = Partition.objects.create( name=s['name'], num=s['num'] )

        th = Theme.objects.all()
        if len(th) == 0:  # база пуста
            for s in lst_theme:
                s = Theme.objects.create( name=s['name'], num=s['num'] )

        level = Level.objects.all()
        if len(level) == 0:  # база пуста
            for s in lst_level:
                s = Level.objects.create( name=s['name'], num=s['num'] )


        stud = MathUser.objects.all()
        if len( stud ) == 0:  #  база пуста
            for s in lst_student:
                s = MathUser.objects.create(  last_name=s['last_name'], first_name=s['first_name'],
                                         email=s['email'], num_class=int(s['class']), letter_class=s['ch'],
                                         password='1234567890', username=s['username'])
        #print( '********************************************************************************************************* stud-OK')
        # Задачи
        task = Task.objects.all()
        if len(task) == 0:
            for t in lst_task:
                ti = Task.objects.create(  question=t['question'], numtask=t['numtask'], variant=t['variant'],
                                           level_id = t['level_id'], theme_id=t['theme_id']  )
                #print('>>>>>>>>>>>>>> ti.id=',ti.id, type(ti.id))
                t_id = ti.id #Task.objects.get( numtask=ti.id )    #t['numtask']).id
                #print( t_id, type(t_id))
                for v in t['version']:
                    Version.objects.create( npp=v['npp'], answer=v['variant'], correct=v['correct'], task_id=t_id )

        #print('********************************************************************************************************* tsk-OK')
        # уроки
        import random
        stud = MathUser.objects.all()
        tsk = Task.objects.all()

        # Каждому студенту назначается задача.  На которую он случайно отвечает
        for s in stud:
            s_id = s.id
            for t in tsk:
                t_id = t.id
                Lesson.objects.create( answer=random.randint(1,4), student_id=s_id, task_id=t_id  )
        #print('********************************************************************************************************* less-OK')