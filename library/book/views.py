from rest_framework import generics
from .models import Book
from .serializers import BookDetailSerializer, BookListSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = (IsAuthenticated, )

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer

class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )