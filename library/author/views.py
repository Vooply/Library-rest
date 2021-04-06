from rest_framework import generics
from .models import Author
from .serializers import AuthorDetailSerializer, AuthorListSerializer


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer

class AuthorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer