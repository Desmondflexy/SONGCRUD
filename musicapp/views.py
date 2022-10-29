from django.shortcuts import render
from .models import Artiste, Song, Lyric

# Create your views here.


def index(request):
    return render(request, 'musicApp/index.html', {
        # to-be-edited: key-value pairs; django site variables,
    })


