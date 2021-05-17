import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "literal.settings")

app = Celery("literal")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
