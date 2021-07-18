from django.urls import path
from . import views


app_name = 'advertiser_management'
urlpatterns = [
    path('info/', views.InfoView.as_view(), name='advertiserManagement-info'),
    path('ad/create/', views.CreateAdView.as_view(), name='advertiserManagement-ad-create'),
    path('click/<int:pk>/', views.ClickRedirectView.as_view(), name='advertiserManagement-click'),
    path('', views.HomeView.as_view(), name='advertiserManagement-home'),
]
