from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.music.api_endpoint.Genres.GenresRetrieveUpdateDestroyView.serializers import \
    GenresRetrieveUpdateDestroySerializer
from apps.music.models import Genre


class GenresRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresRetrieveUpdateDestroySerializer


__all__ = ('GenresRetrieveUpdateDestroyView',)
