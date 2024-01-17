from rest_framework import serializers
<<<<<<< HEAD

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )
=======
#from product.models.category import Category

from product.models.product import Product, Category
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True) 
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True , many=True) 
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

    class Meta:
        model = Product
        fields = [
<<<<<<< HEAD
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")
=======
            'id',
            'title',
            'description',
            'price',
            'active',
            'category',
            'categories_id',
        ]
    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)

        return product