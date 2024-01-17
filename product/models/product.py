from django.db import models
<<<<<<< HEAD
from .category import Category
=======
from product.models.category import Category
#from django.contrib.auth.models import User  # Certifique-se de importar o modelo User
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
<<<<<<< HEAD
    category = models.ManyToManyField(Category, blank=True)

    
    def __str__(self):
        return self.title
=======
    category = models.ManyToManyField(Category, blank=True) #adicionei category aqui (estava faltando)
    #categories = models.ManyToManyField(Category, blank=True) não fica aqui



>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
