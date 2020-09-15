from factory import django, Faker

from blog.models import Blog


class BlogFactory(django.DjangoModelFactory):
    class Meta:
        model = Blog

    name = Faker('bothify', text='?###??716', letters='АВЕКМНОРСТУХ')
    slug = Faker('slug')
    body = Faker('paragraph', nb_sentences=3)
