from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta

from advertiser_management.models import *

app = Celery()

HOUR = 60 * 60
DAY = 60 * 60 * 24


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # hourly
    sender.add_periodic_task(HOUR, get_hourly_click_view(), name='add every hour')
    # daily
    sender.add_periodic_task(DAY, get_daily_click_view(), name='add every day')


@app.task
def get_hourly_click_view(end_datetime=None):
    ending_point = end_datetime if end_datetime else datetime.now()
    ending_point = ending_point.replace(minute=0, second=0, microsecond=0)
    starting_point = ending_point - timedelta(hours=1)
    click_num = Click.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    view_num = View.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    HourlyClickViewInfo.objects.create(click_num=click_num, view_num=view_num, datetime=starting_point)


@app.task
def get_daily_click_view(end_datetime=None):
    ending_point = end_datetime if end_datetime else datetime.now()
    ending_point = ending_point.replace(minute=0, second=0, microsecond=0)
    starting_point = ending_point - timedelta(days=1)
    click_num = Click.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    view_num = View.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    DailyClickViewInfo.objects.create(click_num=click_num, view_num=view_num, datetime=starting_point)
