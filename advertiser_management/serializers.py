from rest_framework import serializers

from advertiser_management.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    ads = serializers.PrimaryKeyRelatedField(many=True, queryset=Ad.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'ads']


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ad
        # fields = '__all__'
        fields = ['owner', 'title', 'imgURL', 'link', 'theAdvertiser', 'approve']


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'
