from django.urls import path
from apps.pages import views

urlpatterns = [
    path('equipment', views.equipment, name="equipment"),
]