from django.urls import path
from . import views

urlpatterns = [
    path('', views.SteamDeckView.as_view(), name='steamdeck'),
]
