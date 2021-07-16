from django.db import models
from django.db.models import Sum

class BaseAdvertising(models.Model):
	"""docstring for BaseAdvertising"""
	clicks = models.IntegerField()
	views = models.IntegerField()

	def __init__(self,  clicks = 0, views = 0):
		super(BaseAdvertising, self).__init__()
		self.clicks = clicks
		self.views = views

	# def getId():
	# 	return self._id
	# def setId(self, _id_):
	# 	self._id = _id_
	def getClicks(self):
		return self.clicks
	def getViews(self):
		return self.views
	def incClicks(self):
		self.clicks += 1
	def incViews(self):
		self.views += 1
	def describeMe(self):
		return "BaseAdvertising: Class for basic functions needed for advertising"


class Advertiser(BaseAdvertising, models.Model):
	"""docstring for Advertiser"""
	name = models.CharField(max_length = 100)

	def __init__(self, name, clicks = 0, views = 0):
		super(Advertiser, self).__init__()
		self.name = name
		self.clicks = clicks
		self.views = views

	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name

	@staticmethod
	def help():
		return "Help: id is the Advertiser id, name is the Advertiser name, clicks and views are the number of clicks and views of this Advertisers ads. The field total clicks is the sum of all Advertisers clicks."

	@staticmethod
	def getTotalClicks():
		return ItemPrice.objects.aggregate(Sum('price'))

	def incClicks(self):
		self.clicks += 1

	def describeMe(self):
		return "Advertiser: Class containing advertiser info and functions needed for each advertiser"



class Ad(BaseAdvertising, models.Model):
	"""docstring for Ad"""
	title =  models.CharField(max_length = 100)
	imgURL =  models.CharField(max_length = 100)
	link =  models.CharField(max_length = 100)
	theAdvertiser = models.ForeignKey(Advertiser, on_delete = models.CASCADE)

	def __init__(self, title, imgURL, link, theAdvertiser, clicks = 0, views = 0):
		super(Ad, self).__init__()
		self.title = title
		self.clicks = clicks
		self.views = views
		self.imgURL = imgURL
		self.link = link
		self.theAdvertiser = theAdvertiser

	def getTitle(self):
		return self.title
	def setTitle(self, title):
		self.title = title

	def incClicks(self):
		self.clicks += 1
		self.theAdvertiser.incClicks()

	def describeMe(self):
		return "Ad: Class containing ad info and functions needed for each ad"

