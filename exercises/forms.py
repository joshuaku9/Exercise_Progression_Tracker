from django import forms
from . import models
from django.forms import ModelForm
from .models import Exercises


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercises
        fields = ['name', 'weight', 'sets', 'reps', 'user']