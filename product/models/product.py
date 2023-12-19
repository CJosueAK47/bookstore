from django.db import models
from product.models.category import Category
from django.contrib.auth.models import User  # Certifique-se de importar o modelo User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveBigIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=100) #adicionei category aqui (estava faltando)
    categories = models.ManyToManyField(Category, blank=True)


