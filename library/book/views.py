from rest_framework import generics

from common.permissions import IsAdmin, IsAdminOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAdmin,)


class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)
