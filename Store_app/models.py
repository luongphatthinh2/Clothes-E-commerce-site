from enum import auto
from django.db import models
from django.shortcuts import get_object_or_404
from Category_app.models import Category
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name

    def  get_productDetail_url(self):
        # print('debug self.category', self.category)
        # category = get_object_or_404(
        #     Category,
        #     id = self.category
        # )
        return reverse('product_detail',args=[self.category, self.slug])