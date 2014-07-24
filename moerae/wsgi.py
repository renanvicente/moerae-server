"""
WSGI config for moerae project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site
site.addsitedir('../../../lib/python2.7/site-packages')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moerae.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moerae.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
