from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('ads', views.AdList.as_view(), name='advertiserManagement-adList'),
    path('ads/<int:pk>/', views.AdDetail.as_view(), name='advertiserManagement-adiInfo'),
    path('advertisers', views.AdvertiserList.as_view(), name='advertiserManagement-advertiserList'),
    path('advertisers/<int:pk>/', views.AdvertiserDetail.as_view(), name='advertiserManagement-advertiserInfo'),
    path('users/', views.UserViewSet.as_view(), name='advertiserManagement-users'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
