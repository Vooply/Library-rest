# from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookDetailSerializer, BookListSerializer


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer