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
