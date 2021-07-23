from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from advertiser_management.views import *
from advertiser_management.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'advertiser_management'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'advertisers', AdvertiserViewSet, basename='advertiser')
urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
