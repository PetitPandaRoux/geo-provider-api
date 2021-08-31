"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# This will set production as default, but we must still set it with an
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.prod')

application = get_asgi_application()
