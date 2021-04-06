from django.urls import path

from order.views import OrderListView

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
]