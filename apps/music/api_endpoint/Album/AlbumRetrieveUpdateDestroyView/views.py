from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.music.api_endpoint.Album.AlbumRetrieveUpdateDestroyView.serializers import (
    AlbumRetrieveUpdateDestroySerializer,
)
from apps.music.models import Album


class AlbumRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumRetrieveUpdateDestroySerializer


__all__ = ("AlbumRetrieveUpdateDestroyView",)
