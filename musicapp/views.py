from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *


# Create your views here.

def index(request):
    mysongs = Song.objects.all()
    context = {
        'mysongs': mysongs,
    }
    return render(request, 'musicapp/index.html', context)

def add(request):
    artistes = Artiste.objects.all()
    return render(request, 'musicapp/add.html', {
        'artistes': artistes,
    })

def addRecord(request):
    if request.method == "POST":
        title = request.POST['title']
        artiste_id = request.POST['artiste']
        artiste = Artiste.objects.get(pk=int(artiste_id))
        newsong = Song(title=title, artiste=artiste)
        newsong.save()
        return HttpResponseRedirect(reverse('musicapp:index'))

def details(request, id):
    song = Song.objects.get(id=id)
    context = {
        'id': id,
        'title': song.title,
        'artist': song.artiste.getfullname(),
        'date_released': song.date_released,
        'likes': song.likes,
        'all_lyrics': song.related_lyrics.all(),
    }
    return render(request, 'musicapp/details.html', context)

def update(request, id):
    song = Song.objects.get(id=id)
    context = {
        'title': song.title,
        'date_released': song.date_released,
    }
    return render(request, 'musicapp/update.html', context)

def updateRecord(request, id):
    song = Song.objects.get(id=id)
    song.title = request.POST['title']
    song.date_released = request.POST['date_released']
    song.save()
    return HttpResponseRedirect(reverse('musicapp:index'))

def delete(request, id):
    song = Song.objects.get(id=id)
    song.delete()
    return HttpResponseRedirect(reverse('musicapp:index'))

def lyrics(request, id):
    lyrics = Lyric.objects.get(id=id)
    return render(request, 'musicapp/lyrics.html', {
        'lyrics': lyrics.content.split('\n'),
        'source': lyrics.source,
    })