from django.urls import path
from . import views


app_name = 'advertiser_management'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='advertiserManagement-home'),
    path('counter/<int:pk>/', views.ClickRedirectView.as_view(), name='advertiserManagement-click'),
]
