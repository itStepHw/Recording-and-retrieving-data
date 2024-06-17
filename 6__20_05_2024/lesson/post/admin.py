from django.contrib import admin
from .models import Category, Post


# Register your models here.

class AdminCategory(admin.ModelAdmin):
    # list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class AdminPost(admin.ModelAdmin):
    # list_display = ['title']
    search_fields = ['title']
    list_filter = ['title', 'is_published', 'published_date']


admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
