from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "avatar", "password")
