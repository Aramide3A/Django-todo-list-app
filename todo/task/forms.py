from .models import *
from django.forms import ModelForm


class Taskform(ModelForm):
    
    class Meta():
        model = Tasks
        fields = '__all__'
