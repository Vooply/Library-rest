from django.urls import path, include
from .views import *

app_name = 'author'

urlpatterns = [
    path('create/', AuthorCreateView.as_view()),
    path('all/', AuthorListView.as_view()),
    path('update/<int:pk>', AuthorUpdateView.as_view()),
]