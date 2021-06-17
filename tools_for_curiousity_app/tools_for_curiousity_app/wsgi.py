"""
WSGI config for tools_of_curiosity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tools_for_curiosity_app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
