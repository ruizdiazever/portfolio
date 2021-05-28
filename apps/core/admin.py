from django.contrib import admin
from .models import Blog
from .models import Certificates
from .models import Docs
from .models import Curriculum

# Blog
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering','year')

admin.site.register(Blog, BlogAdmin)


# Certificates
class CertificatesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering')

admin.site.register(Certificates, CertificatesAdmin)


# Docs
class DocsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering')

admin.site.register(Docs, DocsAdmin)


# Curriculum
class CurriculumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'updated')

admin.site.register(Curriculum, CurriculumAdmin)
