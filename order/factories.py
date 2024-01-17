import factory
<<<<<<< HEAD
from django.contrib.auth.models import User

=======

from django.contrib.auth.models import User
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
from order.models import Order
from product.factories import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
<<<<<<< HEAD
    email = factory.Faker("pystr")
    username = factory.Faker("pystr")
=======
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

    class Meta:
        model = User

<<<<<<< HEAD

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
=======
class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    #id = factory.Faker('pyint')
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
<<<<<<< HEAD

        if extracted:
            for product in extracted:
                self.product.add(product)


    class Meta:
        model = Order
=======
        if extracted:
            for product in extracted:
                self.product.add(product)
    class Meta:
        model = Order
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
