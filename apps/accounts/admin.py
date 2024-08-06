from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'status', 'avatar')
    search_fields = ('username', 'email')
    list_filter = ('status',)
    ordering = ('username',)