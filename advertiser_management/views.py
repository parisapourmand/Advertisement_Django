from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from advertiser_management.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)