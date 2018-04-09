from django.core.urlresolvers import reverse
from django.db import models

# 3rd party package to handly currency
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(blank=True, null=True, db_index=True, unique=True)

    class Meta:
        ordering = ['-name',]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:category-list', args=[self.slug])

class MenuItem(models.Model):
    category = models.ForeignKey(Category, related_name='menu_items')
    # table ???
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, default='')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_items/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category',]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:list')

