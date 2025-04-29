from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    unit_price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.category})"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    country = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Sale of {self.product.name} in {self.country} on {self.date}"
