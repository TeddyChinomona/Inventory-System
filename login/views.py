from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from loguru import logger

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        logger.info(serializer.data.password)
        serializer.is_valid(raise_exception = True)
        logger.info(serializer.data.password)
        
        return super().create(request, *args, **kwargs)
