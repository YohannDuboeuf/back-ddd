from django.db import models

class Cluster(models.Model):
    label = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class TrackClusterAssignment(models.Model):
    track = models.ForeignKey('spotify_data.Track', on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

class ProductClusterProfile(models.Model):
    product = models.ForeignKey('sales_data.Product', on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    score = models.FloatField()
