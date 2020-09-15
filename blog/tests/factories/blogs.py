from factory import django, Faker, lazy_attribute
from blog.models import Blog

Faker._DEFAULT_LOCALE = 'ru_RU'


class BlogFactory(django.DjangoModelFactory):
    class Meta:
        model = Blog

    name = Faker('bothify', text='?###??716',
                 letters='АВЕКМНОРСТУХ')
    slug = Faker('slug', locale='en_US')
    body = Faker('paragraph', nb_sentences=3)

    @lazy_attribute
    def cost(self):
        return (Faker('pydecimal', left_digits=3, right_digits=2,
                      positive=True, min_value=100,
                      max_value=900).generate({}), 'RUB')
