from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.

def home(request):
    all_albums = Album.objects.all()
    html = ""

    for album in all_albums:
        url = "/app1/" + str(album.id) + ""
        html += '<a href=" ' + url + '">' + album.album_title + '</a> <br>'
    return HttpResponse(html)

def details(request, album_id):
    return HttpResponse(album_id)
