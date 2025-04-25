from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category,Program
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
@admin.register(Program)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug':('name',)}