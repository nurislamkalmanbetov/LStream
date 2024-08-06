from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image', 'created_at', 'download_count', 'views_count', 'rating', 'category']