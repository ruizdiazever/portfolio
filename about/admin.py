from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(About, AboutAdmin)