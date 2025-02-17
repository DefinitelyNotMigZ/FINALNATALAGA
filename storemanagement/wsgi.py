"""
WSGI config for sample_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get("ENVIRONMENT", "DEV")

if environment == "PROD":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storemanagement.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storemanagement.settings.dev")

application = get_wsgi_application()
