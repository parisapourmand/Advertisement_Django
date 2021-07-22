from django.shortcuts import render, get_object_or_404
from django.views import generic
from advertiser_management.forms import InfoForm
from django.http import HttpResponse

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions

from advertiser_management.serializers import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class ClickRedirectView(generic.RedirectView):
#     permanent = False
#     query_string = True
#     pattern_name = 'ad-click'
#
#     def get_redirect_url(self, *args, **kwargs):
#         ad = get_object_or_404(Ad, pk=kwargs['pk'])
#         Click.objects.create(ad=ad, ipaddress=self.request.ip)
#         return ad.link

