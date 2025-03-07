# transpiler/celery.py

import os
from celery import Celery

# Set the default Django settings module for Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transpiler.settings')

app = Celery('transpiler')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps.
app.autodiscover_tasks()
