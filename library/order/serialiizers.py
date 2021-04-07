from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView

from book.models import Book
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreate(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('plated_end_at',)

    def create(self, validated_data):
        view = self.context.get('view')
        book_id = view.kwargs['book_id'] if view else None
        if not book_id:
            raise NotFound('Book with given id not found')
        order = Order.objects.create(book_id=book_id, **validated_data)
        return order

