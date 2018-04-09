from django.contrib import admin

from .models import Category, MenuItem


@admin.register(Category)
class CategoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'available', 'added_on', 'updated']
    prepopulated_fields = {'slug': ('name',)}