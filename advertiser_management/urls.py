from django.urls import path
from . import views

urlpatterns = [
    path('', views.ads, name = 'advertiserManagment-ads'),
]