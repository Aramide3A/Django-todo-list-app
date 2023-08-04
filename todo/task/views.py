from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home_page(request):
    tasks = Tasks.objects.all()
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'task/home.html', context)

def modify_page(request, pk):
    tasks = Tasks.objects.get(id = pk)
    form = Taskform(instance= tasks)

    if request.method == 'POST':
        form = Taskform(request.POST, instance= tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    
    context = { 'form': form }
    return render(request, 'task/modify.html', context)

def delete(request, pk):
    tasks = Tasks.objects.get(id = pk)

    if request.method == 'POST':
        tasks.delete()
        return redirect('/')

    return render(request, 'task/delete.html',  )