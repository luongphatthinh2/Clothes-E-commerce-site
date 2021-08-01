from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug1 = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_category_url(self):
        # print('DEBUG: ', reverse("product_by_category",args = [self.category_name]))
        return reverse("product_by_category",args = [self.category_name])

    def __str__(self) -> str:
        return self.category_name