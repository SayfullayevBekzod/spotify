from rest_framework.generics import CreateAPIView

from apps.music.models import Artist
from apps.music.api_endpoint.Artist.ArtistCreate.serializers import (
    ArtistCreateSerializer,
)


class ArtistCreateView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCreateSerializer


__all__ = ("ArtistCreateView",)
