from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
