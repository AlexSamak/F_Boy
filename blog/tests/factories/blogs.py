from factory import django, Faker, lazy_attribute, post_generation
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

    @post_generation
    def def_test(self, create, extracted, key1, key2, **kwargs):
        if not create:
            return
        print(extracted)
        print(key1)
        print(key2)
        return 48+54
