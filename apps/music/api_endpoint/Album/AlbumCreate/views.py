from rest_framework.generics import CreateAPIView

from apps.music.api_endpoint.Album.serializers import AlbumSerializer
from apps.music.models import Album


class AlbumCreateView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


__all__ = ("AlbumCreateView",)
