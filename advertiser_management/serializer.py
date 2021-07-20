from rest_framework import serializers

from advertiser_management.models import *


class AdvertiserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['name']


class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'imgURL', 'link', 'theAdvertiser', 'approve']


class ClickSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Click
        fields = ['datetime', 'ipaddress', 'ad']


class ViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = View
        fields = ['datetime', 'ipaddress', 'ad']
