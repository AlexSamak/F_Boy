from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BlogTest(APITestCase):
    def test_blog_not_found(self):
        data = {'slug': 'tara'}
        response = self.client.get(reverse('blog-get'), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
