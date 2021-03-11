from .base import *

with open('/home/everdev/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

DEBUG = False

ALLOWED_HOSTS = ['www.everdev.it']