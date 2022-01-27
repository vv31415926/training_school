from django import forms
from .models import *

class NewTaskForm( forms.ModelForm ):
    class Meta:
        model=Task
        fields=['num', 'name', 'comment', 'numclass','set_time']
        widgets = { 'name': forms.Textarea(attrs={'cols': 35, 'rows':5}),
                      'comment': forms.Textarea(attrs={'cols': 35, 'rows': 5})
                    }

class NewVariantForm( forms.ModelForm ):
    class Meta:
        model=Variant
        fields=['question', 'img', 'level']
        widgets = {  'question': forms.Textarea(   attrs={'cols': 35, 'rows': 5}  ),
                    }

class StudentLessonForm( forms.ModelForm ):
    # ошибка: Cannot assign "<QuerySet [<MathUser: Косолапов Сергей, 10А>, <MathUser: Кукушкин Апполинарий, 11Б>]>": "Lesson.student" must be a "MathUser" instance.
    # mathuser = forms.ModelMultipleChoiceField(
    #     queryset=MathUser.objects.filter( is_student=True ),
    #     widget=forms.CheckboxSelectMultiple(),
    #     label = 'Студенты...'
    # )
    class Meta:
        model = Lesson
        fields = ('mathuser',)
        #exclude = ('answer','variant')

class LessonsUserForm( forms.ModelForm ):
    class Meta:
        model=Lesson
        fields=['status', 'answer',  'mathuser']

class NewAnswerForm( forms.ModelForm ):
    class Meta:
        model=Answer
        fields=['name', 'correct']








# class TaskForm( forms.ModelForm ):
#     #test = forms.BooleanField()
#     #question = forms.CharField( widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
#     class Meta:
#         model=Task
#         fields=['numtask', 'variant', 'question', 'comment', 'numclass','level','theme','img']
#         widgets = {  'question': forms.Textarea(attrs={'cols': 35, 'rows':5})    }
#

#
# class NewVersionForm( forms.ModelForm ):
#     class Meta:
#         model=Version
#         fields=['answer', 'correct']
#         #fields = ['npp', 'answer', 'correct', 'task']
#         #widgets = {'task': forms.Textarea(attrs={'cols': 35, 'rows': 5})}
#
#
# class VersionForm( forms.ModelForm ):
#     class Meta:
#         model=Version
#         fields=['answer', 'correct' ]
#
# class TaskUsersForm( forms.Form ):
#     question = forms.CharField( widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}) )
#
# class PartitionForm( forms.ModelForm ):
#     num = forms.IntegerField()
#
#     class Meta:
#         model=Partition
#         fields=['num', 'name' ]