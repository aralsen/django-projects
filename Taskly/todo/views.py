from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.contrib import messages
from django_ratelimit.decorators import ratelimit

from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm, UpdateProfileForm
from .models import Task, Profile


# Create your views here.
def home(request):
    return render(request, "index.html")


@login_required(login_url="login")
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    return render(request, "profile/dashboard.html", context=context)


@ratelimit(key='user_or_ip', rate='10/m')
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            profile = Profile.objects.create(user=user)
            messages.success(request, "Account created successfully")
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
@ratelimit(key='user_or_ip', rate='30/m')
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
@ratelimit(key='user_or_ip', rate='50/m')
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


@login_required(login_url="login")
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)
    form_2 = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        if form_2.is_valid():
            form_2.save()
            return redirect("dashboard")

    context = {"form": form, "form_2": form_2}

    return render(request, "profile/profile-management.html", context=context)


@login_required(login_url="login")
def delete_account(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user.delete()
        return redirect("")

    return render(request, "profile/delete-account.html")
