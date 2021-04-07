from django.db import models, DataError, IntegrityError
from django.utils import timezone

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
import datetime


def get_plated_end():
    return timezone.now() + timezone.timedelta(days=15)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='orders')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name='book')

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """

        return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'book': self.book,
            'created_at': str(self.created_at),
            'end_at': str(self.end_at) if self.end_at else self.end_at,
            'plated_end_at': str(self.plated_end_at)
        }

    @staticmethod
    def create(user, book, plated_end_at=None):
        if plated_end_at is None:
            plated_end_at = timezone.now() + timezone.timedelta(days=15)

        try:
            if book.count <= 1:
                raise ValueError
            order = Order.objects.create(user=user, book=book, plated_end_at=plated_end_at)
            book.count -= 1
            return order
        except (DataError, IntegrityError, ValueError):
            return None

    @staticmethod
    def get_by_id(order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    def update(self, plated_end_at=None, end_at=None):
        if plated_end_at:
            self.plated_end_at = plated_end_at
        if end_at:
            self.end_at = end_at
        self.save()

    @staticmethod
    def get_all():
        return list(Order.objects.all())

    @staticmethod
    def get_not_returned_books():
        return [order for order in Order.get_all() if order.end_at is None]

    @staticmethod
    def delete_by_id(order_id):
        try:
            return Order.objects.get(id=order_id).delete()
        except Order.DoesNotExist:
            return None
