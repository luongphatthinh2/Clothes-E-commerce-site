from django.contrib import admin
from Store_app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}


# Register your models here.

admin.site.register(Product, ProductAdmin)
