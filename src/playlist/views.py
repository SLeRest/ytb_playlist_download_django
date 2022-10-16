from django.contrib.auth.models import User

from rest_framework import viewsets, permissions

from playlist.serializers import UserSerializer, SongSerializer
from playlist.models import Song

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
