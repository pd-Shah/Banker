from rest_framework import serializers


class AccountDeleteSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
