from django.shortcuts import render, get_object_or_404
from django.views import generic

from advertiser_management.models import *


class HomeView(generic.ListView):
    template_name = 'advertiser_management/ads.html'
    context_object_name = 'advertisers'

    # queryset = Advertiser.objects.all()
    def get_queryset(self):
        """Return Advertisers."""
        for ad in Ad.objects.all():
            View.objects.create(ad=ad, ipaddress=self.request.META.get('REMOTE_ADDR'))
        return Advertiser.objects.all()


class ClickRedirectView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad-click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.objects.create(ad=ad, ipaddress=self.request.META.get('REMOTE_ADDR'))
        # return ad.link
        return 'https://www.google.com/'


class CreateAdView(generic.CreateView):
    model = Ad
    fields = ['title', 'imgURL', 'link', 'theAdvertiser']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Ad.objects.filter(theAdvertiser=self.user, title=title).exists():
    #         raise form.ValidationError("You have already have an ad with same title.")
    #     return title


# class InfoView(generic.CreateView):
#     model = Ad
#     fields = [all()]
#     Ad.objects.order_by('click__datetime')
#     Ad.objects.order_by('view__datetime')
