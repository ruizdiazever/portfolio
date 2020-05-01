from django.contrib import admin
from django.urls import path, include

from core import views as views_core
from projects import views as views_projects

from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_core.home, name='home'),
    path('projects/', views_projects.projects, name='projects'),
    path('about/', include('about.urls'))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)