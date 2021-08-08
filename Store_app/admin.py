from django.contrib import admin
from Store_app.models import Product,Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'created_date', 'is_active')
    list_editable = ('is_active','variation_value')
    list_filter = ('product', 'variation_category', 'variation_value', 'created_date', 'is_active')

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
