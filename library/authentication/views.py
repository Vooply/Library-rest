from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

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
    permission_classes = (IsAdmin,)
    serializer_class = RegistrationSerializer
