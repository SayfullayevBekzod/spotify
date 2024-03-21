from rest_framework.generics import ListAPIView

from apps.user.api_endpoints.User.UserList.serializers import UserListSerializer
from apps.user.models import User


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


__all__ = ("UserListView",)
