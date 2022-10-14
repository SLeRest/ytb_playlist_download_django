from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created', )

class Song(Base):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(default=None)
    downloaded = models.DateTimeField(default=None) # TODO a verif pour le default

    def __str__(self):
        return self.name

class Playlist(Base):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlaylistSongs(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
