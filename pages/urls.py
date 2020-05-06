from django.urls import path
from . import views

urlpatterns = [
    path('equipment', views.equipment, name="equipment"),
]