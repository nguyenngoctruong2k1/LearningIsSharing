"""
WSGI config for FINALPROJECT project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/NT213.M21.ANTN/FINALPROJECT')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FINALPROJECT.settings")

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FINALPROJECT.settings')
#os.environ('DJANGO_SETTINGS_MODULE', 'FINALPROJECT.settings')
#sys.path.append('/home/ubuntu/NT213.M21.ANTN/venv/lib/python3.9/site-packages')

application = get_wsgi_application()
