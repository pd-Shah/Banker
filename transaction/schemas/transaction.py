from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    branch = serializers.CharField(max_length=64)
    destination = serializers.CharField(max_length=64)
    value = serializers.IntegerField()
