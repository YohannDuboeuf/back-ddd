from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    unit_price = models.FloatField()

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
