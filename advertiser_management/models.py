from django.db import models
from django.db.models import Sum
from django.urls import reverse


class BaseAdvertising(models.Model):
    """docstring for BaseAdvertising"""
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def get_clicks(self):
        return self.clicks

    def get_views(self):
        return self.views

    def inc_clicks(self):
        self.clicks += 1
        self.save()

    def inc_views(self):
        self.views += 1
        self.save()

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

    def get_absolute_url(self):
        return reverse('ad-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def inc_clicks(self):
        self.clicks += 1
        self.theAdvertiser.inc_clicks()
        self.save()

    def describe_me(self):
        return "Ad: Class containing ad info and functions needed for each ad"
