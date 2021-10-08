from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import BranchFilter
from ..models import Branch
from ..permissions import CanCreate
from ..schemas import BranchSerializer


class ViewSetBranch(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet, ):
    filter_class = BranchFilter
    permission_classes = (IsAuthenticated, CanCreate)

    def get_queryset(self):
        return Branch.objects.all()

    def get_serializer_class(self):
        return BranchSerializer
