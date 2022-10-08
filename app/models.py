from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    downloaded = models.DateTimeField(default=None) # TODO a verif pour le default
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    # TODO album associe
    release_date = models.DateField()
    downloaded = models.DateTimeField(default=None) # TODO a verif pour le default
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
