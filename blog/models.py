from django.db import models
from djmoney.models.fields import MoneyField


class Blog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    cost = MoneyField(max_digits=17, decimal_places=2, default=0,
                      default_currency='RUB')
