from datetime import datetime
from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField()

    def getfullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name="related_songs")
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    likes = models.PositiveIntegerField(null=True, blank=True)

    def getSongTitle(self):
        return self.title

    def __str__(self):
        return f"{self.title} - {self.artiste.getfullname()}"


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="related_lyrics")
    content = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"Lyrics for {self.song.artiste.getfullname()}'s {self.song.getSongTitle()} - {self.source}"


