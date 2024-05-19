from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    clients = [
        {'id': 1, 'name': 'John Doe', 'profession': 'Web Developer'},
        {'id': 2, 'name': 'Jane Doe', 'profession': 'Data Scientist'},
        {'id': 3, 'name': 'Jim Doe', 'profession': 'Software Engineer'},
        {'id': 4, 'name': 'Jill Doe', 'profession': 'DevOps Engineer'},
        {'id': 5, 'name': 'Jack Doe', 'profession': 'Network Engineer'},
    ]

    context = {
        'clients': clients
    }

    return render(request, "index.html", context=context)


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")
