from django.contrib import admin
from apps.projects.models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering')

admin.site.register(Projects, ProjectsAdmin)