from django.db import models
from django.db.models import Sum
from datetime import datetime, timedelta
from statistics import mean

# from Yektanet import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


class BaseAdvertising(models.Model):
    """docstring for BaseAdvertising"""

    def describe_me(self):
        return "BaseAdvertising: Class for basic functions needed for advertising"


class Advertiser(BaseAdvertising):
    """docstring for Advertiser"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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

    def describe_me(self):
        return "Ad: Class containing ad info and functions needed for each ad"

    def get_hourly_info(self, starting_point, ending_point):
        hourly_clicks = self.click_set.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
        hourly_views = self.view_set.filter(datetime__gte=starting_point, datetime__lt=ending_point).count()
        hourly_info = {'datetime': starting_point.strftime("%Y-%m-%d %H:%M", ), 'clicks': hourly_clicks,
                       'views': hourly_views}
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

    def get_click_view_rate(self):
        info_list = self.get_total_hourly_info()
        result = {info['datetime']: round(info['clicks'] / info['views'], 2) for info in info_list if
                  info['views'] != 0}
        result_sorted = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result_sorted

    def get_avg_difference(self):
        differences = []
        for v in self.view_set.all():
            for c in self.click_set.all():
                if v.ipaddress == c.ipaddress and c.datetime > v.datetime:
                    differences.append((c.datetime - v.datetime).total_seconds() / 60)
        average_dif = mean(differences)
        return average_dif


class Click(models.Model):
    """docstring for Click"""
    datetime = models.DateTimeField(auto_now=True)
    ipaddress = models.GenericIPAddressField(null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class View(models.Model):
    """docstring for View"""
    datetime = models.DateTimeField(auto_now=True)
    ipaddress = models.GenericIPAddressField(null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create()
