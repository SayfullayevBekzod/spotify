from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.user.api_endpoints.Follow.User.UserFiltiring.serializers import (
    UserListSerializer,
)
from apps.user.models import User


class UserSearchView(ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = [
        "followings",
    ]
    search_fields = [
        "username",
    ]

    def get(self):
        search = self.request.query_params = ["search"]
        queryset = User.objects.all()
        queryset = queryset.filter(username__icontains=search)
        return queryset
