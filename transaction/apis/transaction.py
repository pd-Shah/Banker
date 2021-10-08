from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..logics import create_transaction
from ..models import Transaction
from ..permissions import CanDeposit, CanWithdraw
from ..schemas import TransactionSerializer


class APIViewTransaction(GenericAPIView):
    permission_classes = (IsAuthenticated, CanDeposit, CanWithdraw)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            destination = request.data.get("destination", None)
            branch = request.data.get("branch", None)
            value = request.data.get("value", None)
            if destination is not None and branch is not None and value is not None:
                create_transaction(request.user, destination, value, branch)
                return Response("the transaction submitted.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Transaction.objects.all()

    def get_serializer_class(self):
        return TransactionSerializer
