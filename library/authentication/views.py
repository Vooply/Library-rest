from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from authentication.models import CustomUser
from authentication.serializers import UserSerializer, RegistrationSerializer
from common.permissions import IsAdmin, IsOwnerOrAdmin


class UserView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdmin,)
    lookup_url_kwarg = 'user_id'


class ListUserView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)


class CreateUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


# class LoginAPIView(APIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#
#     # permission_classes = (IsAuthenticated,)
#
#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),
#             'auth': str(request.auth),
#         }
#         return Response(content)



def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')
