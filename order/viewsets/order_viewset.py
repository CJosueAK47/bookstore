from rest_framework.viewsets import ModelViewSet

from order.models import Order
<<<<<<< HEAD
from order.serializers.order_serializer import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
=======
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
