from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Account
from ..permissions import CanCreate
from ..schemas import AccountCreateSerializer


class ViewSetCreateAccount(mixins.CreateModelMixin,
                           viewsets.GenericViewSet, ):
    permission_classes = (IsAuthenticated, CanCreate)

    def get_queryset(self):
        return Account.objects.all()

    def get_serializer_class(self):
        return AccountCreateSerializer
