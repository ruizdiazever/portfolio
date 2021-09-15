from .base import *

with open('/home/ever/Dropbox/dev/keys/portfolio.txt') as f:
    SECRET_KEY = f.read().strip()

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.9', '0.0.0.0']