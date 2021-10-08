from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..logics import create_account
from ..permissions import CanCreate
from ..schemas import AccountCreateSerializer


class APIViewCreateAccount(GenericAPIView, ):
    permission_classes = (IsAuthenticated, CanCreate)

    def post(self, request, format=None):
        user_id = request.data.get("user", None)
        branch_id = request.user.branch.id
        if user_id is not None and branch_id is not None:
            create_account(user_id, branch_id, )
            return Response("created.", status=status.HTTP_201_CREATED)
        return Response("something is wrong!", status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        return AccountCreateSerializer
