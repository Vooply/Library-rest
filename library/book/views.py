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
# Create your views here.
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from rest_framework.serializers import ModelSerializer
# from rest_framework.viewsets import ModelViewSet

# from book.models import Book
# from order.views import OrderCreateView

#
# class BookSerializer(ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     # lookup_url_kwarg = =
#
#
# app_name = 'books'
#
# router = DefaultRouter()
# router.register(r'', BookViewSet)
#
# urlpatterns = [path('<int:book_id>/order', OrderCreateView.as_view(), name='order')] + router.url
