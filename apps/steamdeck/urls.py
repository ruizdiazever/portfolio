from django.urls import path
from apps.steamdeck import views


urlpatterns = [
    path('', views.SteamDeckView.as_view(), name='steamdeck'),
]
