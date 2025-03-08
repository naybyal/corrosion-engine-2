import os
from django.core.wsgi import get_wsgi_application

# Ensure this matches your intended settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

application = get_wsgi_application()
