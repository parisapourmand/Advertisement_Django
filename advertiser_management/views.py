from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from advertiser_management.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


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


class AdvertiserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdvertiserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
