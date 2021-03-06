from django_filters import FilterSet

from ..models import Account


class AccountFilter(FilterSet):
    class Meta:
        model = Account
        fields = "__all__"
