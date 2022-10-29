from datetime import datetime
from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True)
    age = models.PositiveSmallIntegerField()

    def getfullname(self):
        return self.first_name + self.last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    likes = models.PositiveIntegerField(blank=True)

    def getSongTitle(self):
        return self.title

    def __str__(self):
        return f"{self.title} - {self.artiste.getfullname()}"


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    source = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"Lyrics for {self.song.artiste.getfullname()}'s {self.song.getSongTitle()} - {self.source}"


