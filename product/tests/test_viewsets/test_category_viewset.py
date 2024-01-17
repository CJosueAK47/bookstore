import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

<<<<<<< HEAD
from product.factories import CategoryFactory
from product.models import Category
=======
from product.factories import CategoryFactory, ProductFactory
from product.models import Category, Product
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7


class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")

<<<<<<< HEAD
=======
    # def test_get_all_category(self):
    #     response = self.client.get(
    #         reverse("category-list", kwargs={"version": "v1"}))

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     category_data = json.loads(response.content)
        
    #     print(category_data)
    #     self.assertEqual(category_data["results"]
    #                      [0]["title"], self.category.title)
    
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
    def test_get_all_category(self):
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

<<<<<<< HEAD
        self.assertEqual(category_data["results"]
                         [0]["title"], self.category.title)
=======
    # Certifica de que category_data é uma lista
        self.assertIsInstance(category_data, list)
    
    # Se a lista contém dicionários de categorias
        self.assertEqual(category_data[0]["title"], self.category.title)

>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

    def test_create_category(self):
        data = json.dumps({"title": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")

        self.assertEqual(created_category.title, "technology")