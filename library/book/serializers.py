from rest_framework import serializers
from .models import Book


class BookDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors', 'user')

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'authors', 'user')