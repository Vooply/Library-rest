from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('url', 'name', 'surname', 'patronymic', 'author_books')
        extra_kwargs = {
            'author_books': {'view_name': 'book:book_detail'},
            'url': {'view_name': 'author:author_detail'},
        }

