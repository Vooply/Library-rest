from rest_framework import generics

from common.permissions import IsAdmin, IsAdminOrReadOnly
from .models import Author
from .serializers import AuthorSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = (IsAdmin,)


class AuthorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly,)
