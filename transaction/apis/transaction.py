from rest_framework import mixins
from rest_framework import viewsets

from ..filters import TransactionFilter
from ..models import Transaction
from ..schemas import TransactionSerializer


class ViewSetTransaction(mixins.ListModelMixin,
                         viewsets.GenericViewSet, ):
    filter_class = TransactionFilter

    def get_queryset(self):
        return Transaction.objects.all()

    def get_serializer_class(self):
        return TransactionSerializer
