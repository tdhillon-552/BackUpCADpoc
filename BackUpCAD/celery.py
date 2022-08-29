import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackUpCAD.settings')

app = Celery('BackUpCAD')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_calls': {
        'task': 'BackUpDispatch.tasks.get_active_calls',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()
