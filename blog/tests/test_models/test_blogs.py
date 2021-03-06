# from django.urls import reverse
from factory.faker import faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from blog.models import Blog
from blog.tests.factories.blogs import BlogFactory


# add SLUG URL variant
class BlogTest(APITestCase):
    def test_blog_not_found(self):
        data = {'slug': 'random'}
        url = reverse('blog-detail', args=(data['slug'],))
        # url = reverse('blog-detail', kwargs={'pk': 9999})
        print(f'TEST=1: {url}')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_blog_found(self):
        name = 'TEST1'
        slug = 'test1'
        body = 'test TST test TET1'
        blog = Blog.objects.create(name=name, body=body, slug=slug)
        data = {'slug': blog.slug}
        # url = reverse('blog-detail', args=(blog.slug,))
        # print(url)
        url = reverse('blog-detail', kwargs={'pk': blog.id})
        # url = reverse('blog-detail', kwargs={'slug': blog.slug})
        print(f'TEST=2: {url}')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('slug'), blog.slug)

    def test_blog_factory_found(self):
        blog = BlogFactory()
        print(f'TEST=3:\nBlog name: {blog.name}\nBlog body:'
              f' {blog.body}\nBlog slug: {blog.slug}\nBlog cost: {Blog.cost} ')
        data = {'slug': blog.slug}
        print(f'TEST=3: blog id={blog.id}')
        # url = reverse('blog-get', args=(blog.slug,))
        url = reverse('blog-detail', kwargs={'pk': blog.id})
        print(f'TEST=3: blog URL={url}')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('slug'), blog.slug)

    def test_hundrend_blogs(self):
        for i in range(10):
            BlogFactory()
        url = reverse('blog-list')
        print(f'TEST=4: {url}')
        for i in Blog.objects.all():
            print(f'Name: {i.name} Cost: {i.cost}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_blog_Z(self):
        blog = BlogFactory(name='Z',
                           def_test='Check wonderful decorator!!!',
                           def_test__key1=159753,
                           def_test__key2='CHUDO!!!')
        # url = reverse('blog-get', args=(blog.slug,))
        url = reverse('blog-detail', kwargs={'pk': blog.id})
        print(f'TEST=5: {url}')
        response = self.client.get(url, data={'slug': blog.slug})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('name'), "Z")

    def test_one(self):
        prop = "username"
        fake = faker.Faker()
        print(fake.profile(fields=[prop])[prop])


