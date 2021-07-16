from django.shortcuts import render
# from . import models
from advertiser_management.models import BaseAdvertising, Advertiser, Ad

advertiser1 = Advertiser(1, "name1") 
advertiser2 = Advertiser(2, "name2")	
ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
advertisers = [advertiser1, advertiser2]

def ads(request):

	context = {
		'advertisers': advertisers
	}
	return render(request, 'advertiser_management/ads.html', context)