__author__ = 'Pias Tanmoy'

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello')