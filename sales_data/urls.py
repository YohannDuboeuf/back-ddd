from django.urls import path
from sales_data.views import (
    ProductListView,
    SaleListView,
    SaleByCountryView,
    TopSalesByCountryView,
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('sales/', SaleListView.as_view(), name='sale-list'),
    path('sales/country/<str:country>/', SaleByCountryView.as_view(), name='sale-by-country'),
    path('sales/top/<str:country>/', TopSalesByCountryView.as_view(), name='top-sales-by-country'),
]
