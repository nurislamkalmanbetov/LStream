from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date_created', 'streamer', 'game', 'live', 'live_url', 'viewers']

@admin.register(Clip)
class ClipAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date_created', 'streamer', 'stream', 'clip_url']

