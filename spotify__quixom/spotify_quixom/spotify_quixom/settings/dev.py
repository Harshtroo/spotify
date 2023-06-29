import os

from .base import *  # noqa


DEBUG = True
ALLOWED_HOSTS = ["*"]
DEV = DEBUG

INSTALLED_APPS += ("debug_toolbar",)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "spotify_quixom.db",
    }
}

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

SECRET_KEY = "devel"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []


AUTH_PASSWORD_VALIDATORS = []
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "harsh.vekariya@trootech.com"
EMAIL_HOST_PASSWORD = "mcnj@3dn1@"