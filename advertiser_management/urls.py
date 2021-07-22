from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'advertiser_management'
urlpatterns = [
    # path('click/<int:pk>/', views.ClickRedirectView.as_view(), name='advertiserManagement-click'),

    path('', views.AdList.as_view(), name='advertiserManagement-home'),
    path('<int:pk>/', views.AdDetail.as_view(), name='advertiserManagement-info'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
