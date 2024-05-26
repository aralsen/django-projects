from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateTaskForm
from .models import Task


# Create your views here.
def home(request):
    return render(request, "index.html")


@login_required(login_url="login")
def dashboard(request):
    return render(request, "profile/dashboard.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}

    return render(request, "register.html", context=context)


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"form": form}

    return render(request, "login.html", context=context)


def logout(request):
    auth.logout(request)
    return redirect("")


@login_required(login_url="login")
def create_task(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("view-tasks")

    context = {"form": form}

    return render(request, "profile/create-task.html", context=context)


@login_required(login_url="login")
def view_tasks(request):
    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user)
    context = {"task": task}

    return render(request, "profile/view-tasks.html", context=context)


@login_required(login_url="login")
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)

    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("view-tasks")

    context = {"form": form}

    return render(request, "profile/update-task.html", context=context)


@login_required(login_url="login")
def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("view-tasks")

    return render(request, "profile/delete-task.html")
