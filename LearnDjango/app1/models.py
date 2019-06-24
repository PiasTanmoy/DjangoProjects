from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField
    album_title = models.CharField
    genre = models.CharField
    album_logo = models.CharField


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title_type = models.CharField
    song_title = models.CharField
