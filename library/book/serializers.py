from rest_framework import serializers

from author.models import Author
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all(), required=False
    )

    class Meta:
        model = Book
        fields = ('id', 'url', 'name', 'description', 'count', 'authors')
        extra_kwargs = {
            'url': {'view_name': 'book:book_detail'},
        }
