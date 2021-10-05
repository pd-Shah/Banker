from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "*",
]
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
