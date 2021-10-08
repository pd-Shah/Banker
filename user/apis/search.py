from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import UserFilter
from ..models import User
from ..permissions import CanSearch
from ..schemas import UserSerializer


class ViewSetUser(mixins.ListModelMixin,
                  viewsets.GenericViewSet, ):
    filter_class = UserFilter
    permission_classes = (IsAuthenticated, CanSearch)

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
