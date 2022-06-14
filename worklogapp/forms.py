from django import forms
from .models import Task, TaskComment

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'

class TaskCommentForm(forms.ModelForm):
    class Meta:
        model=TaskComment
        fields=('taskCommentDescription',)