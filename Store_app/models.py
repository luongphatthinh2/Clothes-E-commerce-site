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
    def get_variations(self,varation_type):
        variation_list = []
        variations = self.variation_set.filter(variation_category=varation_type,is_active=True)
        for variation in variations:
            variation_list.append(variation.variation_value)
        return variation_list
    def get_color(self):
        return self.get_variations('color')

    def get_size(self):
        return self.get_variations('size')


variation_category_choice =(
    ('color','color'),
    ('size', 'size'),
)
class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active =  models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.variation_category}: {self.variation_value}"
        # return {self.variation_category:self.variation_value }