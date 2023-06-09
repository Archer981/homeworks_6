import factory.django

from ads.models import Ad, Category
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('name')
    email = factory.Faker('email')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = factory.Faker('name')
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 1000
    is_published = False

