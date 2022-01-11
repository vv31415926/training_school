from django import forms
from .models import *

class TaskForm( forms.ModelForm ):
    #test = forms.BooleanField()
    #question = forms.CharField( widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    class Meta:
        model=Task
        fields=['numtask', 'variant', 'question', 'comment', 'numclass','level','theme','img']
        widgets = {  'question': forms.Textarea(attrs={'cols': 35, 'rows':5})    }

class NewTaskForm( forms.ModelForm ):
    class Meta:
        model=Task
        fields=['numtask', 'variant', 'question', 'comment', 'numclass','level','theme','img']
        widgets = {  'question': forms.Textarea(attrs={'cols': 35, 'rows':5})    }

class NewVersionForm( forms.ModelForm ):
    class Meta:
        model=Version
        fields=['answer', 'correct']
        #fields = ['npp', 'answer', 'correct', 'task']
        #widgets = {'task': forms.Textarea(attrs={'cols': 35, 'rows': 5})}


class VersionForm( forms.ModelForm ):
    class Meta:
        model=Version
        fields=['answer', 'correct' ]

class TaskUsersForm( forms.Form ):
    question = forms.CharField( widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}) )
