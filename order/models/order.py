from django.db import models
from django.contrib.auth.models import User

from product.models import Product

class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
