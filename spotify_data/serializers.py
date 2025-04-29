from rest_framework import serializers
from spotify_data.models import Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
