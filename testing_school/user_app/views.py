from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from math_app.models import *
from .forms import *

class UserLoginView( LoginView ):
    # form_class = LoginForm    ошибка
    template_name = 'user_app/login.html'
    success_url = reverse_lazy('mathapp:index')

class UserLogoutView( LogoutView ):
    success_url = reverse_lazy('mathapp:index')

class UserRegisterView( CreateView ):
    model= MathUser   # ?
    template_name = 'user_app/register.html'
    form_class = RegisterForm #UserCreationForm    # стандарт django
    success_url = reverse_lazy( 'mathapp:index' )


class UsersTable( UserPassesTestMixin, ListView ):
    model = MathUser
    template_name = 'user_app/table_users.html'
    context_object_name = 'users'
    #success_url = reverse_lazy('userapp:users_table')

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['nametable'] = 'Список пользователей'
        return context

    # def get_queryset(self):
    #     return MathUser.objects.filter( is_student=True  )
    def test_func(self):  # UserPassesTestMixin
        return self.request.user.is_superuser

# def select_user( request ):
#     if request.method == 'POST':
#         form = SelectUserForm( request.POST )
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect( 'mathapp:tasks_table')
#     else:
#         form = SelectUserForm()
#
#     return render( request, 'name.html', {'form': form})

class SelectUser( ListView ):
    model = MathUser
    form_class = SelectUserForm
    template_name = 'user_app/select_users.html'
    #context_object_name = 'users'
    #success_url = reverse_lazy('userapp:users_table')

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['nametable'] = 'Список пользователей'

        users = MathUser.objects.all()
        lst_data = []
        for item in users:
            id = item.id
            dic = {'users': item, 'select': False,
                   }
            lst_data.append(dic)
        context['users'] = lst_data
        return context

def test_view( request ):
    if request.method == 'POST':
        print('----------- POST')
        formset = SomeFormSet(  request.POST  )
        #form = TestForm(  request.POST )
        if formset.is_valid():
        #if form.is_valid():
            print( '------valid------ ' )
            d = formset.cleaned_data
            print( type(d) )
            for item in d:
                print( 'sel=',item['sel'], 'stud=',item['stud'] )
            return HttpResponseRedirect('/select_user/')
            # print(type(form))
            # print( form.cleaned_data )
            #f = formset.cleaned_data
            #print(f['stud'])
            #print(f['sel'])
            # for f in form.cleaned_data:
            #     print( f.sel )
            #return HttpResponseRedirect(  '/select_user/' )
        else:
            print('------valid------ ERROR ')
    else:
        print('----------- GET')
        formset = FormSet()
    return render( request, 'user_app/test.html', {'formset':formset} )


# class UserLessons( ListView ):
#     model = Lesson
#     template_name = 'math_app/lesson.html'
#     context_object_name = 'student_lessons'
#     pk_url_kwarg = 'student_id'
#
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#         context['title'] = 'уроки'
#         context['obj'] = self.get_queryset()[0]
#         context['namepage'] = 'студент: ' + self.get_queryset()[0].student.last_name+' '+self.get_queryset()[0].student.name
#         return context
#
#     def get_queryset(self):
#         #print( '============',self.kwargs.keys() )
#         return Lesson.objects.filter( student_id=self.kwargs['student_id'] )







# class ShowUser( ListView ):
#     form_class = UserForm
#     template_name = 'math_app/student.html'
#     context_object_name = 'student_one'
#     pk_url_kwarg = 'student_id'
#
#     def get_context_data( self, *, object_list=None, **kwargs ):
#         context = super().get_context_data( **kwargs )
#
#         context['title'] = 'Студент'
#         context['obj'] = self.get_queryset()[0]
#
#         return context
#
#     def get_queryset(self):
#         return Student.objects.filter( pk=self.kwargs['student_id'] )