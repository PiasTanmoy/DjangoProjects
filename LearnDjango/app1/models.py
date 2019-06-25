from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=30, default='')
    album_title = models.CharField(max_length=30, default='')
    genre = models.CharField(max_length=30, default='')
    album_logo = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.album_title + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title_type = models.CharField(max_length=30, default='')
    song_title = models.CharField(max_length=30, default='')
