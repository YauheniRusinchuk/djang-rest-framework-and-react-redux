from rest_framework import viewsets, permissions
from src.models.order.models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.orders.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
