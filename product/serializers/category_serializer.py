from rest_framework import serializers
<<<<<<< HEAD
from product.models.category import Category

=======

from product.models.category import Category
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
<<<<<<< HEAD
            "title",
            "slug",
            "description",
            "active",
        ]

=======
            'title',
            'slug',
            'description',
            'active',
        ]
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
        extra_kwargs = {'slug': {'required': False}}