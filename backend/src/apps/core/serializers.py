from rest_framework import serializers
from src.models.order.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'title',
            'description',
            'owner'
        ]
