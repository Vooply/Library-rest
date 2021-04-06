from django.urls import path, include
from .views import *
# from rest_framework import routers

app_name = 'book'

urlpatterns = [
    path('create/', BookCreateView.as_view()),
    path('all/', BookListView.as_view()),
    path('update/<int:pk>', BookUpdateView.as_view()),
]