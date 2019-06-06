from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt, mpld3

from .models import Exercises
from .forms import ExerciseForm

# Create your views here.

@login_required(login_url="/accounts/login/")
def exercise_list(request, template_name='exercises/exercise_list.html'):
    exercises = Exercises.objects.filter(user=request.user)
    data = {}
    data['object_list'] = exercises
    #for i in exercises:
     #   print(request.user, i.weight for i in exercises)
    return render(request, template_name, data)

def exercise_create(request, template_name='exercises/exercise_form.html'):
    if request.method == "POST":  
        form = ExerciseForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('exercises:exercise_list')  
        else:
            print('Form not valid')
    else:  
        form = ExerciseForm()  
    return render(request, template_name, {'form': form})

def exercise_update(request, pk, template_name='exercises/exercise_form.html'):
    exercise = get_object_or_404(Exercises, pk=pk)
    form = ExerciseForm(request.POST or None, instance=exercise)
    if form.is_valid():
        form.save()
        return redirect('exercises:exercise_list')
    return render(request, template_name, {'form': form})

def exercise_delete(request, pk, template_name='exercises/exercise_delete.html'):
    exercise = get_object_or_404(Exercises, pk=pk)
    if request.method=='POST':
        exercise.delete()
        return redirect('exercises:exercise_list')
    return render(request, template_name, {'object': exercise})

def exercise_graph(request, template_name='exercises/graph.html'):
    exercises = Exercises.objects.filter(user=request.user)
    data = []
    weight=[]
    for i in range(0,len(exercises)):
        data.append(exercises[i].name)
        weight.append(exercises[i].weight)
    fig, ax = plt.subplots()
    rects1 = ax.bar(data,weight)
    #ax.set_xticklabels(data)
    mpld3.show()
    mpld3.close('all')
    return render(request, template_name)
