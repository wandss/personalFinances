from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from .serializers import UserSerializer



class LoginAPIView(APIView):
    """This view authenticates user using default django's auth system,
    creates a token using rest_framework_jwt. It has been created only to
    add more data in the response.
    """

    permission_classes = [AllowAny]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class= UserSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)

        username = request.data.get('username')
        password = request.data.get('password')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user = authenticate(username=username, password=password)

        if not user:
            content = {'non_field_errors':
                       ["Unable to log in with provided credentials."]}

            return Response(content, status=status.HTTP_400_BAD_REQUEST,)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        data = {'token':token, 'username':user.username}

        return Response(data, status=status.HTTP_200_OK)
