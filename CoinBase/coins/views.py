from django.shortcuts import render

# Create your views here.
from .models import Coin
from .serializers import serialize_apples
from django.http import JsonResponse


def coin_list(request):
    coins = Coin.objects.all()
    return JsonResponse(serialize_apples(coins), safe=False)
