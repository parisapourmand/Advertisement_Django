from rest_framework import serializers
from django.contrib.auth.models import User

from advertiser_management.models import *


class UserSerializer(serializers.ModelSerializer):
    ads = serializers.PrimaryKeyRelatedField(many=True, queryset=Ad.objects.all())
    advertisers = serializers.PrimaryKeyRelatedField(many=True, queryset=Advertiser.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'ads', 'advertisers']


class AdvertiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Advertiser
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ad
        fields = '__all__'


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'
