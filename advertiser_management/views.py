import json

from django.shortcuts import render, get_object_or_404
from django.views import generic
from advertiser_management.forms import InfoForm
from django.http import HttpResponse
from django.db.models import Count
from datetime import datetime

from advertiser_management.models import *


class HomeView(generic.ListView):
    template_name = 'advertiser_management/ads.html'
    context_object_name = 'advertisers'

    # queryset = Advertiser.objects.all()
    def get_queryset(self):
        """Return Advertisers."""
        for ad in Ad.objects.all():
            View.objects.create(ad=ad, ipaddress=self.request.ip)
        return Advertiser.objects.all()


class ClickRedirectView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.objects.create(ad=ad, ipaddress=self.request.ip)
        # return ad.link
        return 'https://www.google.com/'


class CreateAdView(generic.CreateView):
    model = Ad
    fields = ['title', 'imgURL', 'link', 'theAdvertiser']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InfoFormView(generic.FormView):
    template_name = 'advertiser_management/info.html'
    form_class = InfoForm

    # success_url = '/thanks/'

    def form_valid(self, form):
        info = form.get_info()
        return HttpResponse(info)
