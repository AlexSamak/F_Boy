from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Blog
from blog.tests.factories.blogs import BlogFactory


class BlogTest(APITestCase):
    def test_blog_not_found(self):
        data = {'slug': 'random'}
        url = reverse('blog-get', args=('random',))
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_blog_found(self):
        name = 'TEST1'
        slug = 'test1'
        body = 'test TST test TET1'
        blog = Blog.objects.create(name=name, body=body, slug=slug)
        data = {'slug': blog.slug}
        url = reverse('blog-get', args=(blog.slug,))
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('slug'), blog.slug)

    def test_blog_factory_found(self):
        blog = BlogFactory()
        data = {'slug': blog.slug}
        url = reverse('blog-get', args=(blog.slug,))
        print(f'name={blog.name};\nslug={blog.slug};\nbody={blog.body}\n\n')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('slug'), blog.slug)

    def test_hundrend_blogs(self):
        for i in range(100):
            BlogFactory()
        url = reverse('blog-all')
        response = self.client.get(url)
        print(len(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)

    def test_blog_Z(self):
        blog = BlogFactory(name='Z')
        url = reverse('blog-get', args=(blog.slug,))
        response = self.client.get(url, data={'slug': blog.slug})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('name'), "Z")