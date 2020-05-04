from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering','year')

admin.site.register(Blog, BlogAdmin)