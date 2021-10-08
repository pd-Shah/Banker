from rest_framework import serializers


class WithdrawSerializer(serializers.Serializer):
    branch = serializers.CharField(max_length=64)
    value = serializers.IntegerField()
