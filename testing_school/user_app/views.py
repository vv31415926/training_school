from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from rest_framework.authtoken.models import Token

from .models import *
from math_app.models import *
from .forms import *
from math_app.forms import *

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

class StudentTable( UserPassesTestMixin, ListView ):
    model = MathUser
    template_name = 'user_app/table_users.html'
    context_object_name = 'users'
    #success_url = reverse_lazy('userapp:users_table')
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs ):
        context = super().get_context_data( **kwargs )
        context['nametable'] = 'Список пользователей'
        return context
    def get_queryset(self):
        #return MathUser.objects.filter(is_student=True)
        #return MathUser.student_objects.all()     #.filter(is_student=True)
        return MathUser.objects.filter( is_student=True )
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

class UserProfileView(  DetailView ):
    template_name = 'user_app/profile.html'
    model = MathUser
    context_object_name = 'mathuser'

def update_token( request ):
    user = request.user
    if user:
        #t = Token.objects.get(user=user)
        t = Token.objects.filter(user=user)
        if len(t) > 0:
            t[0].delete()
    Token.objects.create( user=user )
    return HttpResponseRedirect( reverse( 'user_app:user_profile', kwargs={'pk':user.pk} )  )


# def test_view( request ):
#     if request.method == 'POST':
#         print('----------- POST')
#         formset = SomeFormSet(  request.POST  )
#         #form = TestForm(  request.POST )
#         if formset.is_valid():
#         #if form.is_valid():
#             print( '------valid------ ' )
#             d = formset.cleaned_data
#             print( type(d) )
#             for item in d:
#                 print( 'sel=',item['sel'], 'stud=',item['stud'] )
#             return HttpResponseRedirect('/select_user/')
#             # print(type(form))
#             # print( form.cleaned_data )
#             #f = formset.cleaned_data
#             #print(f['stud'])
#             #print(f['sel'])
#             # for f in form.cleaned_data:
#             #     print( f.sel )
#             #return HttpResponseRedirect(  '/select_user/' )
#         else:
#             print('------valid------ ERROR ')
#     else:
#         print('----------- GET')
#         formset = FormSet()
#     return render( request, 'user_app/test.html', {'formset':formset} )



# class lessonVariantCreate( CreateView ):
#     model = Lesson
#     template_name = 'math_app/variant_detail.html'
#     success_url = ''
#     form_class = StudentLessonForm
#
#     def post(self, request, *args, **kwargs):
#         print('>>>>>>>>>>>>>>>>> kwargs[variant_id]=', kwargs['variant_id'])
#         self.variant_id = kwargs['variant_id']
#         return super().post( request, *args, **kwargs )
#     def form_valid(self, form):
#         print('>>>>>>>>>>>>>>>>> form_valid' )
#         #print('>>>>>>>>>>>>>>>>> form=', form )
#         #print('>>>>>>>>>>>>>>>>> form=', form.)
#         variant = get_object_or_404( Variant, pk=self.variant_id )
#         form.instance.variant = variant
#         self.task_id = variant.task_id
#         return super().form_valid( form )
#     def get_success_url(self):
#         #return reverse( 'mathapp:variant_detail', kwargs={'variant_id':self.variant_id } )
#         return reverse('mathapp:variants_task', kwargs={'task_id': self.task_id})
# class UserLessons( ListView ):
#     model = Lesson
#     template_name = 'math_app/lessons_user.html'
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