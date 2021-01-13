"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from decouple import config
from django.core.wsgi import get_wsgi_application

if config('ENV') == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.prod')
    
application = get_wsgi_application()
