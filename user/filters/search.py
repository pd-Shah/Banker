from django_filters import FilterSet
from django_filters.filters import OrderingFilter

from ..models import User


class UserFilter(FilterSet):
    ordering = OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
        )
    )

    class Meta:
        model = User
        fields = {
            'national_code': ['exact', ],
            'phone_number': ['exact', ],
            'is_active': ['exact', ],
            'is_staff': ['exact', ],
            'account__is_active': ['exact', ],
            'account__balance': ['lt', 'gt'],
        }
