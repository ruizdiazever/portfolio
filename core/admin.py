from django.contrib import admin
from .models import Blog
from .models import Certificates

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering','year')

admin.site.register(Blog, BlogAdmin)

class CertificatesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering')

admin.site.register(Certificates, CertificatesAdmin)