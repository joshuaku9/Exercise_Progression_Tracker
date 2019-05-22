from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.forms import ModelForm

from .models import Exercises

# Create your views here.
class ExerciseForm(ModelForm):
    class Meta:
        model = Exercises
        fields = ['id', 'name']

def exercise_list(request, template_name='exercises/exercise_list.html'):
    exercises = Exercises.objects.all()
    data = {}
    data['object_list'] = exercises
    return render(request, template_name, data)

def exercise_create(request, template_name='exercises/exercise_form.html'):
    form = ExerciseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('exercises:exercise_list')
    return render(request, template_name, {'form': form})

def exercise_update(request, pk, template_name='exercises/exercise_form.html'):
    exercise = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('exercises:exercises_list')
    return render(request, template_name, {'form': form})

def exercise_delete(request, pk, template_name='exercises/exercise_delete.html'):
    exercise = get_object_or_404(blog_posts, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('exercises:exercise_list')
    return render(request, template_name, {'object': post})