from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from datetime import date
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt, mpld3

from .models import Exercises
from .forms import ExerciseForm

# Create your views here.

@login_required(login_url="/accounts/login/")
def exercise_list(request, template_name='exercises/exercise_list.html'):
    exercises = Exercises.objects.filter(user=request.user, date_created=date.today())
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

def exercise_bargraph(request, template_name='exercises/bargraph.html'):
    exercises = Exercises.objects.filter(user=request.user, date_created=date.today())
    data = []
    weight=[]
    for i in range(0,len(exercises)):
        data.append(exercises[i].name)
        weight.append(exercises[i].weight)
    fig, ax = plt.subplots()
    rects1 = ax.bar(data,weight)
    ax.set_ylabel('Weight')
    ax.set_xlabel('Exercise') 
    ind = range(0, len(data))
    ax.set_xticks(ind)
    ax.set_xticklabels(data)   
    mpld3.show()
    mpld3.close('all')
    return render(request, template_name)

def exercise_linegraph(request, template_name='exercises/linegraph.html'):
    ex_sqm = Exercises.objects.filter(user=request.user, name='Squat - Moderate')
    ex_sqh = Exercises.objects.filter(user=request.user, name='Squat - Heavy')
    ex_ib = Exercises.objects.filter(user=request.user, name='Incline Bench')
    ex_dead = Exercises.objects.filter(user=request.user, name='Deadlift')

    w_sqm=[]
    w_sqh=[]
    w_ib=[]
    w_dead=[]
    t_sqm=[]
    t_sqh=[]
    t_ib=[]
    t_dead=[]
    for i in range(0,len(ex_sqm)):
        w_sqm.append(ex_sqm[i].weight)
        t_sqm.append(ex_sqm[i].date_created)
    for i in range(0,len(ex_sqh)):
        w_sqh.append(ex_sqh[i].weight)
        t_sqh.append(ex_sqh[i].date_created)
    for i in range(0,len(ex_ib)):
        w_ib.append(ex_ib[i].weight)
        t_ib.append(ex_ib[i].date_created)
    for i in range(0,len(ex_dead)):
        w_dead.append(ex_dead[i].weight)
        t_dead.append(ex_dead[i].date_created)
   
    fig, ax = plt.subplots()
    ax.plot(t_sqm,w_sqm, label='Squat - Moderate')
    ax.plot(t_sqh,w_sqh, label='Squat - Heavy')
    ax.plot(t_ib,w_ib, label='Incline Bench')
    ax.plot(t_dead,w_dead, label='Deadlift')
    ax.set_ylabel('Weight')
    ax.set_xlabel('Date')
    ax.legend()  
    mpld3.show()
    mpld3.close('all')
    return render(request, template_name)

