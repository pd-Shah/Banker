from rest_framework import serializers

from ..models import Transaction


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'branch',
            'value',
        )
