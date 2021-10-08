from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from ..logics import create_token


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = create_token(user)
        if token:
            return Response({
                'token': token.key,
            })
        return Response({
            "msg": "your account is not activate"
        })
