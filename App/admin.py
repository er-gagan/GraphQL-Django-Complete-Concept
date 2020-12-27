from django.contrib import admin
from .models import Singer,Song
# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Phone', 'Email']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Duration', 'Published_at', 'written_by']