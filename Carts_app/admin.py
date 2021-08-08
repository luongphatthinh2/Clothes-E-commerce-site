from django.contrib import admin
from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    # list_editable = ('is_active','variation_value')
    # list_filter = ('product', 'variation_category', 'variation_value', 'created_date', 'is_active')

# Register your models here.
admin.site.register(models.Cart)
admin.site.register(models.CartItem,CartAdmin)