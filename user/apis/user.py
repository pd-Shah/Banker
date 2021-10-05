from rest_framework import viewsets

from ..models import User
from ..schemas.user import UserSerializer


class ViewSetUser(
    viewsets.GenericViewSet):

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
