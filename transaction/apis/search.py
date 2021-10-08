from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import SearchTransactionFilter
from ..models import Transaction
from ..permissions import CanSearch
from ..schemas import SearchTransactionSerializer


class ViewSetTransaction(mixins.ListModelMixin,
                         viewsets.GenericViewSet, ):
    filter_class = SearchTransactionFilter
    permission_classes = (IsAuthenticated, CanSearch)

    def get_queryset(self):
        return Transaction.objects.all()

    def get_serializer_class(self):
        return SearchTransactionSerializer
