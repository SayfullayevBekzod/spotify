from rest_framework.generics import ListAPIView

from apps.music.models import Artist
from apps.music.api_endpoint.Artist.serializers import ArtistSerializer


class ArtistListView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


__all__ = ("ArtistListView",)
