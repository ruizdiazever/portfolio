from django.urls import path
from apps.contact import views

urlpatterns = [
    path('', views.contact, name="contact"),
]