from rest_framework import serializers

from ..models import Account


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
