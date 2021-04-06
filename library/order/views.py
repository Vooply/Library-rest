from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.permissions import IsAdmin, IsOwnerOrAdmin
from order.models import Order
from order.serialiizers import OrderSerializer, OrderCreate


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdmin,)
    serializer_class = OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderCreate

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        print(data)
        data.update({'book': kwargs['book_id']})
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyListOrderView(ListAPIView):
    permission_classes = (IsOwnerOrAdmin,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user_id=self.kwargs['user_id'])
