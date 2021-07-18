from django.shortcuts import render, get_object_or_404
from django.views import generic

from advertiser_management.models import BaseAdvertising, Advertiser, Ad
# from .forms import CreateAdForm


class HomeView(generic.ListView):
    template_name = 'advertiser_management/ads.html'
    context_object_name = 'advertisers'

    # queryset = Advertiser.objects.all()
    def get_queryset(self):
        """Return Advertisers."""
        for advertiser in Advertiser.objects.all():
            advertiser.inc_views()
        return Advertiser.objects.all()


class ClickRedirectView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.inc_clicks()
        return 'https://www.google.com/'


class CreateAdView(generic.CreateView):
    model = Ad
    fields = ['title', 'imgURL', 'link', 'theAdvertiser']
