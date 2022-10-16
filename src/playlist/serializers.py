from django.contrib.auth.models import User
from rest_framework import serializers

from playlist.models import Song

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Song
        fields = ('name', 'artist', 'album', 'release_date', 'downloaded',
                    'created', 'updated')
