from celery import shared_task
from advertiser_management.models import *


@shared_task(queue='counting')
def get_hourly_click_view(end_datetime=None):
    ending_point = end_datetime if end_datetime else datetime.now()
    ending_point = ending_point.replace(minute=0, second=0, microsecond=0)
    starting_point = ending_point - timedelta(hours=1)
    click_num = Click.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    view_num = View.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    HourlyClickViewInfo.objects.create(click_num=click_num, view_num=view_num, datetime=starting_point)


@shared_task(queue='counting')
def get_daily_click_view(end_datetime=None):
    ending_point = end_datetime if end_datetime else datetime.now()
    ending_point = ending_point.replace(minute=0, second=0, microsecond=0)
    starting_point = ending_point - timedelta(days=1)
    click_num = Click.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    view_num = View.objects.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
    DailyClickViewInfo.objects.create(click_num=click_num, view_num=view_num, datetime=starting_point)
