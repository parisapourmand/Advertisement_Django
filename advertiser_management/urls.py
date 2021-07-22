from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('adlist', views.AdList.as_view(), name='advertiserManagement-adList'),
    path('ad/<int:pk>/', views.AdDetail.as_view(), name='advertiserManagement-adiInfo'),
    path('advertiserlist', views.AdvertiserList.as_view(), name='advertiserManagement-advertiserList'),
    path('advertiser/<int:pk>/', views.AdvertiserDetail.as_view(), name='advertiserManagement-advertiserInfo'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
