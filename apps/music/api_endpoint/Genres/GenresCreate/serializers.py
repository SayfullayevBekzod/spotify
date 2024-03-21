from rest_framework.serializers import ModelSerializer

from apps.music.models import Genre


class GenresCreateSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
