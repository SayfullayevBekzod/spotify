from rest_framework.serializers import ModelSerializer

from apps.music.models import Genre


class GenresListSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
