from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('spotify_data.urls')),
    path('api/', include('sales_data.urls')),
    path('api/', include('recommendation.urls')),
]
