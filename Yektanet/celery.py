import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')
app = Celery('Yektanet', broker='amqp://localhost')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
CELERY_TIMEZONE = 'Asia/Tehran'

HOUR = 60 * 60
DAY = 60 * 60 * 24

app.conf.beat_schedule = {
    'info per hour': {
        'task': 'advertiser_management.tasks.get_hourly_click_view',
        'schedule': HOUR
    },
    'info per day': {
        'task': 'advertiser_management.tasks.get_daily_click_view',
        'schedule': DAY
    },
}
