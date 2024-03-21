from rest_framework.generics import ListAPIView, get_object_or_404

from apps.user.api_endpoints.Follow.UserFollowers.serializers import (
    FollowerListSerializer,
)
from apps.user.models import User


class UserFollowersView(ListAPIView):
    serializer_class = FollowerListSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        user = get_object_or_404(User, pk=pk)
        return user.followers.all()


__all__ = ("UserFollowersView",)
