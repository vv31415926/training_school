from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
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

class TasksPage( UserPassesTestMixin, ListView ):
    model = Task
    template_name = 'math_app/table_tasks.html'
    # context_object_name = 'tasks' - не нужно т.к. определяется в context['tasks'] =  lst_data
    #raise_exception = False

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )

        tasks = Task.objects.all()
        lst_data = []
        for item in tasks:
            id = item.id
            vers = Version.objects.filter(task=id)
            lst = []
            for i, v in enumerate(vers):
                lst.append(v)
            dic = {'task': item, 'vers': lst, 'themenum': item.theme.num,
                   'themename': item.theme.name, 'partname': item.theme.partition.name,
                   'partnum': item.theme.partition.num,
                   'taskid':id
                  }
            lst_data.append(dic)

            context['title']= 'Задачи'
            context['nametable'] = 'Список задач'
            context['tasks'] =  lst_data

        return context

    def test_func(self):
        #print(  'правило суперпользователь >>>>>>>>>>>>>>>>>>>>>>>>',self.request.user.is_superuser )
        #print(' > ', self.request.user, ' > ', type(self.request.user), ' > ', self.request )
        return self.request.user.is_superuser

class ShowTask( UpdateView ):
    form_class = TaskForm
    template_name = 'math_app/task.html'
    context_object_name = 'task_one'
    pk_url_kwarg = 'task_id'
    success_url = reverse_lazy('mathapp:tasks_table')

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Задача.'
        context['image'] = self.get_queryset()[0].img
        return context

    def get_queryset(self):
        return Task.objects.filter( pk=self.kwargs['task_id'] )

class NewTask( CreateView ):
    model = Task
    form_class = NewTaskForm
    template_name = 'math_app/new_task.html'
    #context_object_name = 'task'
    success_url = reverse_lazy( 'mathapp:tasks_table' )

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Задача'
        return context

class NewVersion( CreateView ):
    model = Version
    form_class = NewVersionForm
    template_name = 'math_app/new_version.html'
    #context_object_name = 'version'
    success_url = reverse_lazy( 'mathapp:tasks_table' )

    #Version.objects.create( '')

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['task_id'] = self.kwargs['task_id']
    #     return initial

    def form_valid(self, form):  # для заполнения поля task_id по текущей задаче
        self.object = form.save( commit=False )
        self.object.task_id = self.kwargs['task_id']
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Версии ответов'
        #print('----------------------------',self.kwargs['task_id'])
        context['taskid'] = self.kwargs['task_id']
        return context

class ShowVersion( UpdateView ):
    form_class = VersionForm
    template_name = 'math_app/version.html'
    context_object_name = 'version'
    pk_url_kwarg = 'version_id'
    def get_context_data( self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['title'] = 'Весии ответов'
        #context['obj'] = self.get_queryset()[0]    дает context_object_name = 'version_one'
        return context
    def get_queryset(self):
        return Version.objects.filter( pk=self.kwargs['version_id'] )

class UserLessons( ListView ):
    model = Lesson
    template_name = 'math_app/lesson.html'
    context_object_name = 'lessons'
    pk_url_kwarg = 'student_id'

    def get_context_data( self, *, object_list=None, **kwargs ):
        #print( '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',self.kwargs.keys())
        context = super().get_context_data( **kwargs )
        context['title'] = 'уроки'
        context['obj'] = self.get_queryset()[0]

        #context['namepage'] = 'Уроки ' + self.get_queryset()[0].student.last_name+' '+self.get_queryset()[0].student.name
        return context

    def get_queryset(self):
        #print( '============',self.kwargs.keys() )
        return Lesson.objects.filter( student_id=self.kwargs['student_id']  )




# class UserTasks( ListView ):
#     model = Task
#     form_class = TaskUsersForm
#     template_name = 'math_app/user_tasks.html'
#     context_object_name = 'task'
#
#     def get_queryset(self):
#         return Task.objects.all(  )
#
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#         context['title'] = 'Задачи для студентов'
#         return context

# def user_tasks(request):
#     if request.method == 'POST':
#         form = TaskUsersForm( request.POST )
#         if form.is_valid():
#             question = form.cleaned_data['question']
#         else:
#             return render( request, 'math_app/user_tasks.html', { 'title': 'Задачи для студентов' }  )
#     else:  # GET
#         form = TaskUsersForm()
#
#     return render(  request, 'math_app/user_tasks.html', { 'form': form, 'title':'Задачи для студентов' } )