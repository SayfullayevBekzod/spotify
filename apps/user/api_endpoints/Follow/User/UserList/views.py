from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from apps.user.api_endpoints.Follow.User.UserList.serializers import UserListSerializer
# from apps.user.debugger import debugger
from apps.user.models import User


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    # @method_decorator(cache_page(60 * 10))
    # @debugger
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)


__all__ = ("UserList",)
