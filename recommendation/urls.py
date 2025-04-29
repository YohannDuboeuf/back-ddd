from django.urls import path
from recommendation.views import InsightByCountryView

urlpatterns = [
    path('insights/<str:country>/', InsightByCountryView.as_view(), name='recommandation-insights-country'),
]
