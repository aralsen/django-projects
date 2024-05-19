from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Review


# Create your views here.
def home(request):
    query_all = Task.objects.all()

    context = {
        "tasks": query_all
    }

    return render(request, "index.html", context=context)


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")
