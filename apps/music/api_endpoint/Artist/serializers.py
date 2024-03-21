from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "avatar", "fullname", "followers")
