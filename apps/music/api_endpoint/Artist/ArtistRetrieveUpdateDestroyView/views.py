from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.music.api_endpoint.Artist.ArtistRetrieveUpdateDestroyView.serializers import (
    ArtistRetrieveUpdateDestroySerializer,
)
from apps.music.models import Artist


class ArtistRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistRetrieveUpdateDestroySerializer


__all__ = ("ArtistRetrieveUpdateDestroyView",)
