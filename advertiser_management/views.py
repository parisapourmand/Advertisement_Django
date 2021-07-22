from rest_framework import generics

from advertiser_management.serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Ad.objects.all()
    serializer_class = AdSerializer

# class ClickRedirectView(generic.RedirectView):
#     permanent = False
#     query_string = True
#     pattern_name = 'ad-click'
#
#     def get_redirect_url(self, *args, **kwargs):
#         ad = get_object_or_404(Ad, pk=kwargs['pk'])
#         Click.objects.create(ad=ad, ipaddress=self.request.ip)
#         return ad.link
