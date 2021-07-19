from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Count
import itertools
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


def date_hour(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%x %H")


class InfoView(generic.ListView):

    def get_queryset(self):
        objs = Ad.objects.all().order_by("click__datetime")
        groups = itertools.groupby(objs, lambda x: date_hour(x.click__datetime))
        for group, matches in groups:
            print(group, "TTL:", Count(1 for _ in matches))
        # for group, matches in groups:
        #     print(group, "TTL:", Count(1 for _ in matches))
        #
        # result = Ad.objects.annotate(the_count=Count('click__datetime'))
        # return result
