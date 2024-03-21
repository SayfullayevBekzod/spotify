from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "followings",
            "artist_following",
            "first_name",
        )
