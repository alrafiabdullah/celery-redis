from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cache_celery.settings')
app = Celery('cache_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    # Executes everynight at 11:00 p.m.
    'delete-every-night-task': {
        'task': 'tasks.delete',
        'schedule': crontab(hour=23, minute=0),
    },
    'delete-every-five-minutes-task': {
        'task': 'tasks.delete',
        'schedule': crontab(minute='2'),
    },
}
app.conf.timezone = 'Asia/Dhaka'

app.autodiscover_tasks()
