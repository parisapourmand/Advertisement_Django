from django.shortcuts import render
from advertiser_management.models import BaseAdvertising, Advertiser, Ad

advertiser1 = Advertiser.objects.create(name = "name1") 
advertiser2 = Advertiser.objects.create(name = "name2")	
ad1 = Ad.objects.create(title = "title1", imgURL = "img-url1", link = "link1", advetiser = advertiser1)
ad2 = Ad.objects.create(title = "title2", imgURL = "img-url2", link = "link2", advetiser = advertiser2)
advertisers = [advertiser1, advertiser2]

def ads(request):
	context = {
		'advertisers': advertisers
	}
	return render(request, 'advertiser_management/ads.html', context)