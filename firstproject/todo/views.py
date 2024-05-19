from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.
def home(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view-tasks")

    context = {"form": form}

    return render(request, "create-task.html", context=context)


def view_tasks(request):
    tasks = Task.objects.all()

    context = {"tasks": tasks}

    return render(request, "view-tasks.html", context=context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("view-tasks")

    context = {"form": form}

    return render(request, "update-task.html", context=context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("view-tasks")

    context = {"object": task}

    return render(request, "delete-task.html", context=context)
