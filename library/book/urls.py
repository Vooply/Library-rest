from django.urls import path, include
from .views import *

app_name = 'book'

urlpatterns = [
    path('create/', BookCreateView.as_view()),
    path('all/', BookListView.as_view()),
    path('update/<int:pk>', BookUpdateView.as_view()),
]