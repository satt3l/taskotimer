from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from tasks.models import Task

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/details.html', {'task': task})


def new(request):
    return render(request, 'tasks/new.html')
