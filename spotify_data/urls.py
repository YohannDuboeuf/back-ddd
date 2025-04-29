from django.urls import path
from spotify_data.views import TrackListView, TrackByCountryView, TopTracksByCountryView

urlpatterns = [
    path('tracks/', TrackListView.as_view(), name='track-list'),
    path('tracks/country/<str:country>/', TrackByCountryView.as_view(), name='track-by-country'),
    path('tracks/top/<str:country>/', TopTracksByCountryView.as_view(), name='top-tracks-by-country'),
]
