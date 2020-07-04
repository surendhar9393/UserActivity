from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
import jwt
from rest_framework_jwt.settings import api_settings
from rest_framework import exceptions
from django.utils.translation import ugettext as _

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class TokenAuthentication(BaseJSONWebTokenAuthentication):
    def get_jwt_value(self, request):
        return request.META.get('HTTP_TOKEN')