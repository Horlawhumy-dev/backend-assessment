import logging

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from django.contrib.auth.models import User


logger = logging.getLogger('task_management')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        logger.info(f"ID: {token.user_id} logs in with token: {token.key}")
        return Response({'token': token.key, 'id': token.user_id})

class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logger.info(f"ID: {request.user.id} logs out succesfully")
        return Response(status=204)
