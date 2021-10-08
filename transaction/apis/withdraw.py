from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..logics import create_withdraw
from ..models import Transaction
from ..permissions import CanWithdraw
from ..schemas import WithdrawSerializer


class APIViewWithdraw(GenericAPIView):
    permission_classes = (IsAuthenticated, CanWithdraw)

    def post(self, request, format=None):
        serializer = WithdrawSerializer(data=request.data)
        if serializer.is_valid():
            branch = request.data.get("branch", None)
            value = request.data.get("value", None)
            if branch is not None and value is not None:
                create_withdraw(request.user, value, branch)
                return Response("the transaction submitted.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Transaction.objects.all()

    def get_serializer_class(self):
        return WithdrawSerializer
