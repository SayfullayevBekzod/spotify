from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.api_endpoints.Follow.UserFollowings.serializers import (
    UserFollowingsSerializer,
)
from apps.user.models import User


class UserFollowingsView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserFollowingsSerializer(user.followings.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


__all__ = ("UserFollowingsView",)
