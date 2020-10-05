from rest_framework import viewsets
from blog.models import Blog
from blog.serializer import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    #lookup_field = 'slug' - if needed attribute slug in URL
    #lookup_field = 'pk' - default
