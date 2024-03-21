from rest_framework.fields import UUIDField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.music.models import Artist


class ArtistSerializer(Serializer):
    artistId = UUIDField()
