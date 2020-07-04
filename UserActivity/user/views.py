from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from UserActivity.user.middleware import CsrfExemptSessionAuthentication
from UserActivity.user.authentication import *
from UserActivity.user.models import User
from .serializers import UserSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


@permission_classes([])
class UserLogin(generics.RetrieveAPIView):
    """
    method to provide authentication token
    for an user.
    """
    permission_classes = (AllowAny,)
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def generate_auth_token(self, user):
        # Generating the JWT Token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def post(self, request):

        data = request.data
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data='Email / password is required.')
        user = authenticate(email=email, password=password)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data='Incorrect email or password')
        login(request, user)
        token = self.generate_auth_token(user)
        response = {
            'token': token,
            'user_name': user.real_name
        }
        return Response(status=status.HTTP_200_OK, data=response)


class UserDetail(generics.RetrieveAPIView):
    def get(self, request):
        users = User.objects.all()
        response = {
            "ok": True,
            "members": UserSerializer(users, many=True).data
        }
        return Response(status=status.HTTP_200_OK, data=response)

