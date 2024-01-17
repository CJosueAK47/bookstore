<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
<<<<<<< HEAD
router.register(r"product", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
=======
router.register(r'product', viewsets.ProductViewSet, basename='product')
router.register(r"category", viewsets.CategoryViewSet, basename="category")
urlpatterns = [
    path('', include(router.urls)),
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
]