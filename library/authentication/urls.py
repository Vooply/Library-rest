from django.urls import path

from authentication.views import UserView, ListUserView, CreateUserView
from order.views import MyListOrderView

app_name = 'users'

urlpatterns = [
    path('', ListUserView.as_view(), name='users_list'),
    path('user/<int:user_id>', UserView.as_view(), name='user_profile'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('user/<int:user_id>/orders', MyListOrderView.as_view(), name='user_orders'),
]
