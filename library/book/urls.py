from django.urls import path, include

from order.views import OrderCreateView
from .views import *

app_name = 'book'

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='create_book'),
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>', BookUpdateView.as_view(), name='book_detail'),
    path('<int:book_id>/order', OrderCreateView.as_view(), name='order')
]
