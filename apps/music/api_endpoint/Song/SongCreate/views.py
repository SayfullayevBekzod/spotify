from rest_framework.generics import CreateAPIView

from apps.music.api_endpoint.Song.SongCreate.serializers import SongCreateSerializer
from apps.music.models import Song


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


__all__ = ("SongCreateView",)
