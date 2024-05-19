from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    name = "GUEST"
    context = {'name': name}
    return render(request, "index.html", context=context)


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")
