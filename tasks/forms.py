from dataclasses import fields
from django.forms import ModelForm
from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']