from rest_framework import serializers
from sales_data.models import Product, Sale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Pour afficher les détails du produit

    class Meta:
        model = Sale
        fields = '__all__'