from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'created_at', 'download_count', 'views_count', 'rating', 'category']
