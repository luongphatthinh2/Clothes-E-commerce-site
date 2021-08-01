from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug1': ('category_name',)
    }
    list_display = ('category_name', 'slug1')

# Register your models here.
admin.site.register(models.Category, CategoryAdmin)
