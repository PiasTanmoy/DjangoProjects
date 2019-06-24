__author__ = 'Pias Tanmoy'

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hi' : 'This is me'})

def eggs(request):
    return HttpResponse("<h1>Eggs are good!!!</h1>")

def home2(request):
    return render(request, 'home2.html')