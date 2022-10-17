from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    artist = models.CharField(max_length=255, null=True, default=None)
    album = models.CharField(max_length=255, null=True, default=None)
    release_date = models.DateField(null=True, default=None)
    downloaded = models.DateTimeField(null=True, default=None)
    song_data = models.BinaryField(null=True, default=None)
    format = models.CharField(null=True, max_length=20) # TODO a list of choice and it can't be mull
    youtube_url = models.CharField(max_length=255) # TODO check if valid url
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('created', )
        db_table = 'song'

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('created', )
        db_table = 'playlist'

class PlaylistSongs(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        db_table = 'playlist_songs'
