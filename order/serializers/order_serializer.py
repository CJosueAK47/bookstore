from rest_framework import serializers
<<<<<<< HEAD

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
=======
from order.models.order import Order

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True) 
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
<<<<<<< HEAD

    class Meta:
        model = Order
        fields = ["product", "total", "user", "products_id"]
        extra_kwargs = {"product": {"required": False}}

    def create(self, validated_data):
        product_data = validated_data.pop("products_id")
        user_data = validated_data.pop("user")
=======
    
    class Meta:
        model = Order  # Corrigir o modelo para Order, não Product
        fields = ['product', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        user_data = validated_data.pop('user')
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)

<<<<<<< HEAD
        return order
=======
        return order
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
