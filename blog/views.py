from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Blog
from blog.serializer import BlogSerializer


class BlogView(APIView):
   def get(self, request, title):
        try:
            print(title)
            blog = Blog.objects.get(slug=title)
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlogListView(APIView):
    def get(self, request):
        try:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

