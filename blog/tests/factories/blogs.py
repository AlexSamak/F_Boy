from decimal import Decimal
from factory import django, Faker
from blog.models import Blog

Faker._DEFAULT_LOCALE = 'ru_RU'


class BlogFactory(django.DjangoModelFactory):
    class Meta:
        model = Blog

    name = Faker('bothify', text='?###??716',
                 letters='АВЕКМНОРСТУХ')
    slug = Faker('slug', locale='en_US')
    body = Faker('paragraph', nb_sentences=3)
    cost = (Decimal('532.50'), 'RUB')
