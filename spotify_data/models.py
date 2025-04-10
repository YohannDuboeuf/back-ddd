from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    popularity = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()

class CountryTrackTrend(models.Model):
    country = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date = models.DateField()
