from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Song, Playlist, PlaylistSong

class SongListView(ListView):
    model = Song

class SongDetailView(DetailView):
    model = Song

class PlaylistDetailView(DetailView):
    model = Playlist

class PlaylistSongDetailView(DetailView):
    model = PlaylistSong
