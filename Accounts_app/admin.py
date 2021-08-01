from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin



class AccountAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name','username','last_login','is_active','date_joined')
    # list_display_links = ('email','first_name')
    ordering =('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(models.Account,AccountAdmin)