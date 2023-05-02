from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'view_children', 'root')
    fields = ['name', 'url', 'parent']
