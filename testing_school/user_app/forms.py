from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory, modelformset_factory

from .models import *

class LoginForm( forms.ModelForm ):
    class Meta:
        model = MathUser
        fields = ('username', 'password')


class RegisterForm( UserCreationForm ):
    class Meta( UserCreationForm.Meta ):
        model = MathUser
        fields = UserCreationForm.Meta.fields + ('email', 'last_name', 'first_name', 'num_class', 'letter_class')
        # UserCreationForm.Meta.fields  - id, email(переопр), password, last_login, is_superuser, is_staff, is_active, date_joined
        #fields = ('email', 'last_name', 'first_name', 'num_class', 'letter_class')

class UserForm( forms.ModelForm ):
    class Meta:
        model=MathUser
        fields=['last_name', 'first_name', 'email', 'num_class', 'letter_class', 'is_student']

class SelectUserForm( forms.Form ):
    sel = forms.BooleanField(  required=False )
    select = forms.BooleanField(required=False)
    #sel = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    #content = forms.CharField(widget=forms





class TestForm( forms.Form ):
    sel = forms.BooleanField( label='Выбор', required=False )
    stud = forms.CharField( label='студент', max_length=100 )

SomeFormSet = modelformset_factory(  model=MathUser, fields=['last_name', 'first_name', 'num_class', 'letter_class', 'is_student'])
FormSet = SomeFormSet( queryset=MathUser.objects.all() )