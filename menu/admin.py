from django.contrib import admin

from .models import Menu, MenuType

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuType)