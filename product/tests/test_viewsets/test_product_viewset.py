# import json

# from django.urls import reverse
# #from rest_framework.authtoken.models import Token desnecessário
# from rest_framework.test import APIClient, APITestCase
# from rest_framework.views import status

# from order.factories import UserFactory
# from product.factories import CategoryFactory, ProductFactory
# from product.models import Product


# class TestProductViewSet(APITestCase):
#     client = APIClient()

#     def setUp(self):
#         self.user = UserFactory()

#         self.product = ProductFactory(
#             title="pro controller",
#             price=200.00,
#         )

#     def test_get_all_product(self):
#         response = self.client.get(
#             reverse("product-list", kwargs={"version": "v1"}))

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         product_data = json.loads(response.content)

#         self.assertEqual(product_data["results"]
#                          [0]["title"], self.product.title)
#         self.assertEqual(product_data["results"]
#                          [0]["price"], self.product.price)
#         self.assertEqual(product_data["results"]
#                          [0]["active"], self.product.active)

#     def test_create_product(self):
#         category = CategoryFactory()
#         data = json.dumps(
#             {"title": "notebook", "price": 800.00,
#                 "categories_id": [category.id]}
#         )

#         response = self.client.post(
#             reverse("product-list", kwargs={"version": "v1"}),
#             data=data,
#             content_type="application/json",
#         )

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         created_product = Product.objects.get(title="notebook")

#         self.assertEqual(created_product.title, "notebook")
#         self.assertEqual(created_product.price, 800.00)


##################### NOVO CÓDIGO ######################################
import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        try:
            # Usa o método json() para acessar os dados JSON diretamente
            product_data = response.json()

            # Verifica se a resposta é uma lista e se há pelo menos um resultado
            self.assertTrue(isinstance(product_data, list))
            self.assertTrue(len(product_data) > 0)

            # Acessa o primeiro item da lista
            first_product = product_data[0]

            self.assertEqual(first_product["title"], self.product.title)
            
            # Remove a conversão para string ao comparar preços
            self.assertEqual(first_product["price"], self.product.price)
            self.assertEqual(first_product["active"], self.product.active)

        except AssertionError:
            # Em caso de falha, imprime os dados para diagnosticar
            print("Failed product_data:", product_data)
            raise  # Ressalta a exceção para que o teste seja marcado como falha

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps(
            {"title": "notebook", "price": 800.00,
                "categories_id": [category.id]}
        )

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")

        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)

