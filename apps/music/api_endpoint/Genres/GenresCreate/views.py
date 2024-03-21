from rest_framework.generics import CreateAPIView

from apps.music.api_endpoint.Genres.GenresCreate.serializers import (
    GenresCreateSerializer,
)
from apps.music.models import Genre


class GenresCreateView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresCreateSerializer


__all__ = ("GenresCreateView",)
