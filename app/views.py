from django.shortcuts import render, redirect
from .models import Tasklist
from .forms import TaskForm, UploadFileForm
from django.contrib import messages
from django.http import HttpResponse
from .resources import TaskResource
from import_export import resources
import tablib
import csv
import io

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        print(form)
        items = Tasklist.objects.all
        if form.is_valid():
            form.save()

            #return render(request, 'app/home.html', {'items': items})
        return render(request, 'app/home.html', {'items': items})
    else:
         items = Tasklist.objects.all
         return render(request, 'app/home.html', {'items': items})

def delete(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('home')

def deleteall(request):
    Tasklist.objects.all().delete()
    return redirect('home')

def edit(request, task_id):
    if request.method == 'POST':
        post = get_object_or_404(Tasklist, pk=task_id)
        form = TaskForm(request.POST or None, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
      form = TaskForm()
    return render(request, 'app/edit.html', {'form': form})

def importcsv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('ok')
            csv_data = readcsvraport(form.cleaned_data['file'])
            for index, i in enumerate(csv_data):
                if index > 0:
                   print(i[0])
                   print(i[1])
                   task_main = Tasklist(item=i[0],ended=i[1])
                   task_main.save()
        return redirect('home')
    else:
        form = UploadFileForm()

    return render(request, 'app/import.html', {'form': form})


def readcsvraport(csvfileraw):
    decoded_file = csvfileraw.file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    csv_reader = csv.reader(io_string, delimiter=',', quotechar='"')
    csvlist = list(csv_reader)

    return(csvlist)
