from rest_framework.generics import CreateAPIView, ListAPIView

from apps.music.api_endpoint.Album.serializers import AlbumSerializer
from apps.music.models import Album


class AlbumListView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


__all__ = ("AlbumListView",)
