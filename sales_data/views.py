from rest_framework import generics
from sales_data.models import Product, Sale
from sales_data.serializers import ProductSerializer, SaleSerializer
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Liste de tous les produits
@permission_classes([IsAuthenticated])
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Liste de toutes les ventes
@permission_classes([IsAuthenticated])
class SaleListView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

# Liste des ventes filtrées par pays
@permission_classes([IsAuthenticated])
class SaleByCountryView(generics.ListAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Sale.objects.filter(country=country)

# Top produits vendus dans un pays (agrégés par quantité)
class TopSalesByCountryView(generics.ListAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return (
            Sale.objects
            .filter(country=country)
            .values('product__name', 'product__category')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('-total_quantity')[:10]
        )
