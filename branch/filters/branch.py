from django_filters import FilterSet

from ..models import Branch


class BranchFilter(FilterSet):
    class Meta:
        model = Branch
        fields = {
            'id': ['exact'],
            'title': ['icontains', 'exact'],
        }
