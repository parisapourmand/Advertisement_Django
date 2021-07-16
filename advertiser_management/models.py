from django.db import models


class BaseAdvertising:
	"""docstring for BaseAdvertising"""
	_id = 0
	_clicks = 0
	_views = 0


	def __init__(self):
		super(BaseAdvertising, self).__init__()

	def getId():
		return self._id
	def setId(self, _id_):
		self._id = _id_
	def getClicks(self):
		return self._clicks
	def getViews(self):
		return self._views
	def incClicks(self):
		self._clicks += 1
	def incViews(self):
		self._views += 1
	def describeMe(self):
		return "BaseAdvertising: Class for basic functions needed for advertising"


class Advertiser(BaseAdvertising):
	"""docstring for Advertiser"""
	_name = ""
	_totalclicks = 0

	def __init__(self, _id, name, clicks = 0, views = 0):
		super(Advertiser, self).__init__()
		self._id = _id
		self._name = name
		self._clicks = clicks
		self._views = views
		Advertiser._totalclicks += clicks

	def getName(self):
		return self._name
	def setName(self, name):
		self._name = name

	@staticmethod
	def help():
		return "Help: id is the Advertiser id, name is the Advertiser name, clicks and views are the number of clicks and views of this Advertisers ads. The field total clicks is the sum of all Advertisers clicks."

	@staticmethod
	def getTotalClicks():
		return Advertiser._totalclicks

	def incClicks(self):
		self._clicks += 1
		Advertiser._totalclicks += 1

	def describeMe(self):
		return "Advertiser: Class containing advertiser info and functions needed for each advertiser"



class Ad(BaseAdvertising):
	"""docstring for Ad"""
	_title = ""
	_imgURL = ""
	_link = ""
	_theAdveriser = None

	def __init__(self, _id, title, imgURL, link, theAdvertiser, clicks = 0, views = 0):
		super(Ad, self).__init__()
		self._id = _id
		self._title = title
		self._clicks = clicks
		self._views = views
		self._imgURL = imgURL
		self._link = link
		self._theAdveriser = theAdvertiser

	def getTitle(self):
		return self._title
	def setTitle(self, title):
		self._title = title

	def incClicks(self):
		self._clicks += 1
		self._theAdveriser.incClicks()

	def describeMe(self):
		return "Ad: Class containing ad info and functions needed for each ad"

