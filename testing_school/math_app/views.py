from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.edit import ModelFormMixin

from .models import *
#from  testing_school.user_app import models
#import testing_school.user_app
from .forms import *

def main_page(  request ):
    context = {'title': 'Проверка знаний.',
            }
    return render( request,
                   'math_app/index.html',
                   context=context )

class PartitionsPage( ListView ):
    model = Partition
    template_name = 'math_app/partitions.html'
    context_object_name = 'partitions'
    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Разделы'
        context['namepage'] = 'Темы по разделам'
        return context
    def get_queryset(self):
        return Partition.objects.all().order_by( 'num' )

# Задачи темы
class ShowTaskTheme( ListView ):
    #form_class = TaskForm
    model = Task
    template_name = 'math_app/task_theme.html'
    context_object_name = 'tasks_theme'
    pk_url_kwarg = 'theme_id'
    success_url = reverse_lazy('mathapp:partitions')
    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Задачи'
        context['namepage'] = 'Задачи темы: "'+Theme.objects.get( pk=self.kwargs['theme_id'] ).name+'"'
        context['themeid'] = self.kwargs['theme_id']
        #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> themeid=', self.kwargs['theme_id'] )
        return context
    def get_queryset(self):
        return Task.objects.filter( theme_id=self.kwargs['theme_id'] )

class NewTask( CreateView ):
    model = Task
    form_class = NewTaskForm
    template_name = 'math_app/new_task.html'
    context_object_name = 'task'
    #success_url = reverse_lazy( 'mathapp:tasks_theme', kwargs={'theme_id':kwargs['theme_id']} )

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Задача'
        return context

    def post(self, request, *args, **kwargs ):
        #print( '======================== kwargs[theme_id]=', kwargs['theme_id'])
        self.theme_id = kwargs['theme_id']
        return super().post( request, *args, **kwargs )

    def form_valid(self, form):
        theme = get_object_or_404( Theme, pk=self.theme_id )
        form.instance.theme = theme
        return super().form_valid(form)
    def get_success_url(self ):
        return reverse( 'mathapp:tasks_theme', kwargs={'theme_id':self.theme_id}  )

class VariantsTask( ListView ):
    #form_class = TaskForm
    model = Variant
    template_name = 'math_app/variants_task.html'
    context_object_name = 'variants'
    pk_url_kwarg = 'task_id'
    paginate_by = 3
    #success_url = reverse_lazy('mathapp:tasks_theme')
    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Варианты задачи'
        context['taskid'] = self.kwargs['task_id']
        context['themeid'] = self.kwargs['theme_id']
        #context['image'] = self.get_queryset()[0].img
        return context
    def get_queryset(self):
        return Variant.objects.select_related('level').filter( task_id=self.kwargs['task_id'] )
        #return Variant.objects.filter(task_id=self.kwargs['task_id'])

class NewVariant( CreateView ):
    model = Variant
    form_class = NewVariantForm
    template_name = 'math_app/new_variant.html'
    context_object_name = 'variant'
    #success_url = reverse_lazy( 'mathapp:tasks_theme', kwargs={'theme_id':kwargs['theme_id']} )

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Варианты'
        return context
    def post(self, request, *args, **kwargs ):
        #print('88888888888888888888888888888888888888888888',kwargs['theme_id'],self.kwargs['theme_id']   )
        self.task_id = kwargs['task_id']
        self.theme_id = kwargs['theme_id']
        return super().post( request, *args, **kwargs )
    def form_valid(self, form):
        task = get_object_or_404( Task, pk=self.task_id )
        form.instance.task = task
        return super().form_valid(form)
    def get_success_url(self ):
        return reverse( 'mathapp:variants_task', kwargs={ 'task_id':self.task_id, 'theme_id':self.theme_id  }  )

class VariantAssign( DetailView ):
    model = Variant
    template_name = 'math_app/variant_assign.html'
    context_object_name = 'variant'
    pk_url_kwarg = 'variant_id'
    def get_context_data(self, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['form'] = StudentLessonForm()
        context['themeid'] = self.kwargs['theme_id']
        context['taskid'] = self.kwargs['task_id']
        return context
# -----------------------------------------------------------------------
class LessonTaskCreate( CreateView ):
    model = Lesson

    def post(self, request, *args, **kwargs ):
        self.task_id = kwargs['task_id']
        self.theme_id = kwargs['theme_id']
    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        return context

class lessonVariantCreate( CreateView ):
    model = Lesson
    template_name = 'math_app/variant_detail.html'
    success_url = ''
    form_class = StudentLessonForm

    def post(self, request, *args, **kwargs):
        #print('>>>>>>>>>>>>>>>>> kwargs[variant_id]=', kwargs['variant_id'])
        self.variant_id = kwargs['variant_id']
        return super().post( request, *args, **kwargs )
    def form_valid(self, form):
        variant = get_object_or_404( Variant, pk=self.variant_id )
        form.instance.variant = variant
        self.task_id = variant.task_id
        return super().form_valid( form )
    def get_success_url(self):
        return reverse('mathapp:variants_task', kwargs={ 'task_id': self.task_id ,'theme_id':self.kwargs['theme_id']  })

# уроки выбранного студента - для админа
class LessonsUser( ListView ):
    model = Lesson
    template_name = 'math_app/lessons_user.html'
    form_class = LessonsUserForm
    context_object_name = 'lessons'
    pk_url_kwarg = 'mathuser_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        #print(  "=================", context.keys())
        context['title'] = 'уроки'
        if len(self.get_queryset()) > 0:
            context['namepage'] = self.get_queryset()[0].mathuser
        else:
            context['namepage'] = 'Нет данных'
        return context
    def get_queryset(self):
        return Lesson.objects.select_related('variant','mathuser').filter( mathuser_id=self.kwargs['mathuser_id']  )
        #return Lesson.objects.filter(mathuser_id=self.kwargs['mathuser_id'])

class AssignedLessons( ListView ):
    model = Lesson
    template_name = 'math_app/assigned_lesson.html'
    context_object_name = 'lessons'
    pk_url_kwarg = 'mathuser_id'
    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'уроки'
        if len(self.get_queryset()) > 0:
            context['obj'] = self.get_queryset()[0]
        else:
            context['obj'] = 'Нет данных'
        return context
    def get_queryset(self):
        return Lesson.objects.filter( mathuser_id=self.kwargs['mathuser_id']  )


class NewAnswer( CreateView ):
    model = Answer
    form_class = NewAnswerForm
    template_name = 'math_app/new_answer.html'
    #context_object_name = 'version'
    #success_url = reverse_lazy( 'mathapp:variants_task' )

    def form_valid(self, form):  # для заполнения поля task_id по текущей задаче
        self.object = form.save( commit=False )
        self.object.variant_id = self.kwargs['variant_id']
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Версии ответов'
        context['variantid'] = self.kwargs['variant_id']
        context['themeid'] = self.kwargs['variant_id']
        return context

    def get_success_url(self):
        return reverse('mathapp:variants_task', kwargs={'task_id':self.kwargs['task_id'], 'theme_id':self.kwargs['theme_id'] })






# class UserLessons( ListView ):
#     model = Lesson
#     template_name = 'math_app/user_lessons.html'
#     context_object_name = 'lessons'
#     pk_url_kwarg = 'student_id'
#
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         #print( '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',self.kwargs.keys())
#         context = super().get_context_data( **kwargs )
#         context['title'] = 'уроки'
#         context['obj'] = self.get_queryset()[0]
#
#         #context['namepage'] = 'Уроки ' + self.get_queryset()[0].student.last_name+' '+self.get_queryset()[0].student.name
#         return context
#
#     def get_queryset(self):
#         #print( '============',self.kwargs.keys() )
#         return Lesson.objects.filter( student_id=self.kwargs['student_id']  )





# class TasksPage( UserPassesTestMixin, ListView ):
#     model = Task
#     template_name = 'math_app/table_tasks.html'
#     # context_object_name = 'tasks' - не нужно т.к. определяется в context['tasks'] =  lst_data
#     #raise_exception = False
#
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#
#         tasks = Task.objects.all()
#         lst_data = []
#         for item in tasks:
#             id = item.id
#             vers = Version.objects.filter(task=id)
#             lst = []
#             for i, v in enumerate(vers):
#                 lst.append(v)
#             dic = {'task': item, 'vers': lst, 'themenum': item.theme.num,
#                    'themename': item.theme.name, 'partname': item.theme.partition.name,
#                    'partnum': item.theme.partition.num,
#                    'taskid':id,
#                   }
#             lst_data.append(dic)
#
#             context['title']= 'Задачи'
#             context['nametable'] = 'Список задач'
#             context['tasks'] =  lst_data
#             #context['theme'] = Theme.objects.all()
#
#         return context
#
#     def test_func(self):
#         #print(  'правило суперпользователь >>>>>>>>>>>>>>>>>>>>>>>>',self.request.user.is_superuser )
#         #print(' > ', self.request.user, ' > ', type(self.request.user), ' > ', self.request )
#         return self.request.user.is_superuser
#
# class ShowTask( UpdateView ):
#     form_class = TaskForm
#     template_name = 'math_app/task.html'
#     context_object_name = 'task_one'
#     pk_url_kwarg = 'task_id'
#     success_url = reverse_lazy('mathapp:tasks_table')
#
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#         context['title'] = 'Задача.'
#         context['image'] = self.get_queryset()[0].img
#         return context
#
#     def get_queryset(self):
#         return Task.objects.filter( pk=self.kwargs['task_id'] )
#


#
# class ShowVersion( UpdateView ):
#     form_class = VersionForm
#     template_name = 'math_app/version.html'
#     context_object_name = 'version'
#     pk_url_kwarg = 'version_id'
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#         context['title'] = 'Весии ответов'
#         #context['obj'] = self.get_queryset()[0]    дает context_object_name = 'version_one'
#         return context
#     def get_queryset(self):
#         return Version.objects.filter( pk=self.kwargs['version_id'] )
#


#
# class ThemesPage( ListView ):
#     model = Theme
#     template_name = 'math_app/themes.html'
#     context_object_name = 'themes'
#
#     def get_context_data(self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#         context['title'] = 'Темы'
#         context['namepage'] = 'Темы задач'
#         return context
#






