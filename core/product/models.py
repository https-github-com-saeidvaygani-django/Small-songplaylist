from django.db import models
from star_ratings.models import Rating


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.DurationField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)  # Use a foreign key to the Rating model

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
