from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    popularity = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    valence = models.FloatField(default=0.0)
    tempo = models.FloatField(default=120.0)
    country = models.CharField(max_length=100, default="Unknown")
    date = models.CharField(default="-")

    def __str__(self):
        return f"{self.name} - {self.artist} ({self.country})"
