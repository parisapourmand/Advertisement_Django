from django.db import models
from django.db.models import Sum
from datetime import datetime, timedelta


class BaseAdvertising(models.Model):
    """docstring for BaseAdvertising"""

    def describe_me(self):
        return "BaseAdvertising: Class for basic functions needed for advertising"


class Advertiser(BaseAdvertising):
    """docstring for Advertiser"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @staticmethod
    def help():
        return "Help: id is the Advertiser id, name is the Advertiser name, clicks and views are the number of " \
               "clicks and views of this Advertisers ads. The field total clicks is the sum of all Advertisers clicks."

    @staticmethod
    def get_total_clicks():
        return Advertiser.objects.aggregate(Sum('price'))

    def describe_me(self):
        return "Advertiser: Class containing advertiser info and functions needed for each advertiser"


class Ad(BaseAdvertising, models.Model):
    """docstring for Ad"""
    title = models.CharField(max_length=100)
    imgURL = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    theAdvertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def get_absolute_url(self):
        return ''

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def describe_me(self):
        return "Ad: Class containing ad info and functions needed for each ad"

    def get_hourly_info(self, starting_point, ending_point):
        hourly_clicks = self.click_set.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
        hourly_views = self.view_set.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
        hourly_info = {'datetime': starting_point.strftime("%Y-%m-%d %H:%M",), 'clicks': hourly_clicks, 'views': hourly_views}
        return hourly_info

    def get_total_hourly_info(self):
        total_clicks = self.click_set.count()
        total_views = self.view_set.count()
        hourly_info_list = []
        click_count = 0
        view_count = 0
        ending_point = datetime.now()

        starting_point = ending_point.replace(minute=0, second=0, microsecond=0)
        hourly_info = self.get_hourly_info(starting_point, ending_point)
        hourly_info_list.append(hourly_info)
        click_count += hourly_info['clicks']
        view_count += hourly_info['views']
        ending_point = starting_point

        while click_count in range(total_clicks) and view_count in range(total_views):
            starting_point = ending_point - timedelta(hours=1)
            hourly_info = self.get_hourly_info(starting_point, ending_point)
            hourly_info_list.append(hourly_info)
            click_count += hourly_info['clicks']
            view_count += hourly_info['views']
            ending_point = starting_point

        return hourly_info_list


class Click(models.Model):
    """docstring for Click"""
    datetime = models.DateTimeField(auto_now=True)
    ipaddress = models.GenericIPAddressField(default='000.000.0.0')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class View(models.Model):
    """docstring for View"""
    datetime = models.DateTimeField(auto_now=True)
    ipaddress = models.GenericIPAddressField(default='000.000.0.0')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
