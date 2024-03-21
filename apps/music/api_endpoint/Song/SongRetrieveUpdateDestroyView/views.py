from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.music.api_endpoint.Song.SongRetrieveUpdateDestroyView.serializers import (
    SongRetrieveUpdateDestroySerializer,
)
from apps.music.models import Song


class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongRetrieveUpdateDestroySerializer


__all__ = ("SongRetrieveUpdateDestroyView",)
