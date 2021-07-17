from django.shortcuts import render
from django.views import generic
from advertiser_management.models import BaseAdvertising, Advertiser, Ad

advertiser1 = Advertiser.objects.create(name="name1")
advertiser2 = Advertiser.objects.create(name="name2")
ad1 = Ad.objects.create(title="title1", imgURL="img-url1", link="link1", theAdvertiser=advertiser1)
ad2 = Ad.objects.create(title="title2", imgURL="img-url2", link="link2", theAdvertiser=advertiser2)


class HomeView(generic.ListView):
    template_name = 'advertiser_management/ads.html'
    context_object_name = 'advertiser_list'

    def get_queryset(self):
        """Return Advertisers."""
        for advertiser in Advertiser.objects.all():
            advertiser.inc_views()
        return Advertiser.objects.all()



