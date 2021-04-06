from rest_framework import generics
from .models import Author
from .serializers import AuthorDetailSerializer, AuthorListSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = (IsAuthenticated, )

class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer

class AuthorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )