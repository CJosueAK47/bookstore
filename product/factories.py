import factory

from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker("pystr")

<<<<<<< HEAD

=======
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
<<<<<<< HEAD
            for categories in extracted:
                self.category.add(categories)

    class Meta:
        model = Product
=======
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
