from rest_framework import generics
from rest_framework.permissions import AllowAny

from common.permissions import IsAdmin, IsAdminOrReadOnly
from .models import Book
from .serializers import  BookSerializer


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
