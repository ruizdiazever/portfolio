from django.contrib import admin
from django.urls import path
from core import views as views_core
from projects import views as views_projects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_core.home, name='home'),
    path('projects/', views_projects.projects, name='projects'),
    path('about/', views_core.about, name='about'),
]