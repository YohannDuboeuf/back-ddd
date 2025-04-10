from django.db import models

class CountryRecommendation(models.Model):
    country = models.CharField(max_length=100)
    recommended_product = models.ForeignKey('sales_data.Product', on_delete=models.CASCADE)
    based_on_track = models.ForeignKey('spotify_data.Track', on_delete=models.SET_NULL, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)
