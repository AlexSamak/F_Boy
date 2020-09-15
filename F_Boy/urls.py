from django.contrib import admin
from django.urls import path, include
from blog.views import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('blogs', BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('blog/<slug:title>/', BlogView.as_view(), name="blog-get"),
#     path('blogs/', BlogListView.as_view(), name="blog-all"),
# ]
