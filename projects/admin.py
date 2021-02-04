from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering')

admin.site.register(Projects, ProjectsAdmin)