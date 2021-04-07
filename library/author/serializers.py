from rest_framework import serializers
from .models import Author


class AuthorDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic', 'user')

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic', 'user')