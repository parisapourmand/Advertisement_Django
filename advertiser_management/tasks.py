from celery import Celery

app = Celery('tasks', broker='advertiser_management://guest@localhost//')
