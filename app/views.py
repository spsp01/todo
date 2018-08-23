from django.shortcuts import render, redirect
from .models import Tasklist
from .forms import TaskForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            items = Tasklist.objects.all
            messages.success(request,('Task Added'))
            return render(request, 'app/home.html', {'items': items})
    else:
         items = Tasklist.objects.all
         return render(request, 'app/home.html', {'items': items})

def delete(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('home')