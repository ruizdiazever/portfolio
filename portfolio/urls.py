from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf import settings
from apps.core import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('certificates/', views.certificates, name="certifications"),
    path('docs/', views.docs, name='docs'),
    
    path('projects/', include('apps.projects.urls')),
    path('about/', include('apps.about.urls')),
    path('contact/', include('apps.contact.urls')),
    path('pages/', include('apps.pages.urls')),
    path('steamdeck/', include('apps.steamdeck.urls')),

    # https://stackoverflow.com/questions/9371378/warning-not-found-favicon-ico
    #path(r'^favicon\.ico$',RedirectView.as_view(url='apps/core/static/img/favicon.ico')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)