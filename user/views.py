from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from user.serializers import UserSerializer, LoginSerializer

# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
