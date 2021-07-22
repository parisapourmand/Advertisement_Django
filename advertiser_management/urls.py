from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'advertiser_management'
urlpatterns = [
    # path('click/<int:pk>/', views.ClickRedirectView.as_view(), name='advertiserManagement-click'),

    path('', views.HomeView.as_view(), name='advertiserManagement-home'),
    path('<int:pk>/', views.InfoFormView.as_view(), name='advertiserManagement-info'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
