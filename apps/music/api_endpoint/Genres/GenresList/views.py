from rest_framework.generics import ListAPIView

from apps.music.api_endpoint.Genres.GenresList.serializers import GenresListSerializer
from apps.music.models import Genre


class GenresListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresListSerializer


__all__ = ('GenresListView',)
