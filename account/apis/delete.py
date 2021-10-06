from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..logics import delete_account
from ..permissions import CanDelete
from ..schemas import AccountDeleteSerializer


class APIViewDeleteAccount(GenericAPIView, ):
    permission_classes = (IsAuthenticated, CanDelete)
    serializer_class = AccountDeleteSerializer

    def post(self, request, format=None):
        pk = request.data.get("account_id", None)
        if pk is not None:
            delete_account(pk=pk)
            return Response("deleted.", status=status.HTTP_200_OK)
        return Response("something is wrong!", status=status.HTTP_400_BAD_REQUEST)
