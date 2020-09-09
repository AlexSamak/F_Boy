from django.contrib import admin
from django.urls import path
from blog.views import BlogView, BlogListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<slug:title>/', BlogView.as_view(), name="blog-get"),
    path('blogs/', BlogListView.as_view(), name="blog-all"),
]
