from django.db import models
from product.models.category import Category
#from django.contrib.auth.models import User  # Certifique-se de importar o modelo User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True) #adicionei category aqui (estava faltando)
    #categories = models.ManyToManyField(Category, blank=True) não fica aqui

    def __str__(self):
        return self.title



