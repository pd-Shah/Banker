from django_filters import FilterSet

from ..models import Transaction


class TransactionFilter(FilterSet):
    class Meta:
        model = Transaction
        fields = "__all__"
