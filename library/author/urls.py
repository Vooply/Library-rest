from django.urls import path, include
from .views import *

app_name = 'author'

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='create_author'),
    path('', AuthorListView.as_view(), name='list_author'),
    path('<int:pk>', AuthorUpdateView.as_view(), name='author_detail'),
]