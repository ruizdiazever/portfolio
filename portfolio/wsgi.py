"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os


# SETTING FOR FIX IN PRODUCTION THE 'whitenoise' problem
import socket

codeProduction = 'from whitenoise.django import DjangoWhiteNoise'
codeProduction2 = 'application = DjangoWhiteNoise(application)'

if socket.gethostname()=="omen":
    pass
else:
    codeProduction.read().strip()


# ORIGINAL SETTING
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.base')
application = get_wsgi_application()


# SETTING FOR FIX IN PRODUCTION THE 'whitenoise' problem
if socket.gethostname()=="omen":
    pass
else:
    codeProduction2.read().strip()