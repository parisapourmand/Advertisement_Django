from django.shortcuts import render, get_object_or_404
from django.views import generic
from advertiser_management.forms import InfoForm
from django.http import HttpResponse

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from advertiser_management.models import *
from advertiser_management.serializer import *


class HomeView(APIView):
    pass
    #     for ad in Ad.objects.all():
    #         View.objects.create(ad=ad, ipaddress=self.request.ip)

    # def get(self, request, format=None):
    #     advertisers = Advertiser.objects.all()
    #     serializer = AdvertiserSerializer(advertisers, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = AdvertiserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClickRedirectView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.objects.create(ad=ad, ipaddress=self.request.ip)
        return ad.link


class CreateAdView(generic.CreateView):
    model = Ad
    fields = ['title', 'imgURL', 'link', 'theAdvertiser']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InfoFormView(generic.FormView):
    template_name = 'advertiser_management/info.html'
    form_class = InfoForm

    def form_valid(self, form):
        info = form.get_info()
        return HttpResponse(info)
