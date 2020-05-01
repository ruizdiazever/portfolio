from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    
    path('projects/', include('projects.urls')),
    path('about/', include('about.urls'))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)