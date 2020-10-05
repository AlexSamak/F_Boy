#from django.urls import reverse
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
        #url = reverse('blog-detail', kwargs={'pk': 9999})
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
        #url = reverse('blog-detail', kwargs={'slug': blog.slug})
        print(f'TEST=2: {url}')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('slug'), blog.slug)

    def test_blog_factory_found(self):
        blog = BlogFactory()
        data = {'slug': blog.slug}
        print(f'TEST=3: {blog.id}   {blog.slug}')
        #url = reverse('blog-get', args=(blog.slug,))
        url = reverse('blog-detail', kwargs={'pk': blog.id})
        print(f'TEST=3: {url}')
        print(f'name={blog.name};\nslug={blog.slug};\nbody={blog.body}\n\n')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('slug'), blog.slug)

    def test_hundrend_blogs(self):
        for i in range(10):
            BlogFactory()
        url = reverse('blog-list')
        print(f'TEST=4: {url}')
        for i in Blog.objects.all():
            print(i.cost)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_blog_Z(self):
        blog = BlogFactory(name='Z')
        #url = reverse('blog-get', args=(blog.slug,))
        url = reverse('blog-detail', kwargs={'pk': blog.id})
        print(f'TEST=5: {url}')
        response = self.client.get(url, data={'slug': blog.slug})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('name'), "Z")
