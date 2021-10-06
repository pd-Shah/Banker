from rest_framework import serializers


class AccountDeleteSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
    branch_id = serializers.IntegerField()
