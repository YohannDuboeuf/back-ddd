from rest_framework import generics
from rest_framework.decorators import permission_classes

from spotify_data.models import Track
from spotify_data.serializers import TrackSerializer
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
class TrackListView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

@permission_classes([AllowAny])
class TrackByCountryView(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Track.objects.filter(country=country).order_by('-popularity')

@permission_classes([AllowAny])
class TopTracksByCountryView(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Track.objects.filter(country=country).order_by('-popularity')[:10]
