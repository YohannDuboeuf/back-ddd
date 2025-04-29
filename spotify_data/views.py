from rest_framework import generics
from spotify_data.models import Track
from spotify_data.serializers import TrackSerializer

class TrackListView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackByCountryView(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Track.objects.filter(country=country).order_by('-popularity')

class TopTracksByCountryView(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Track.objects.filter(country=country).order_by('-popularity')[:10]
