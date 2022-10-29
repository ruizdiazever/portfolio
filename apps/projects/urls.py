from django.urls import path
from apps.projects import views

urlpatterns = [
    path('', views.projects, name="projects")
]
