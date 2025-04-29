from rest_framework.views import APIView
from rest_framework.response import Response
from spotify_data.models import Track
from sales_data.models import Sale
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

import pandas as pd
import pycountry

def country_name_to_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_2
    except LookupError:
        return None

def country_code_to_name(code):
    try:
        return pycountry.countries.get(alpha_2=code.upper()).name
    except:
        return None

@permission_classes([IsAuthenticated])
class InsightByCountryView(APIView):
    def get(self, request, country):
        country = country.upper()
        country_code = country

        # --- Partie Tracks (Spotify)
        tracks = Track.objects.filter(country=country_code)
        track_df = pd.DataFrame.from_records(
            tracks.values('name', 'popularity', 'date', 'country')
        )

        if not track_df.empty:
            # Nettoyer la date si besoin
            track_df['month'] = pd.to_datetime(track_df['date'], errors='coerce').dt.to_period('M').astype(str)
            track_df = track_df.dropna(subset=['month'])

            top_tracks = (
                track_df.groupby('month')
                .apply(lambda x: x.sort_values('popularity', ascending=False).head(3)['name'].tolist())
                .to_dict()
            )
        else:
            top_tracks = {}

        # --- Partie Sales (E-commerce)
        full_country_name = country_code_to_name(country_code)
        sales = Sale.objects.none()
        if full_country_name:
            sales = Sale.objects.filter(country__iexact=full_country_name).select_related('product')

        sales_data = [
            {
                'month': sale.date.strftime('%Y-%m'),
                'category': sale.product.category,
                'quantity': sale.quantity
            }
            for sale in sales
        ]
        sales_df = pd.DataFrame(sales_data)

        if not sales_df.empty:
            top_categories = (
                sales_df.groupby('month')
                .apply(lambda x: x.groupby('category')['quantity'].sum().sort_values(ascending=False).head(3).index.tolist())
                .to_dict()
            )
        else:
            top_categories = {}

        # --- Fusion finale par mois
        months = set(top_tracks.keys()).union(set(top_categories.keys()))
        insights = []
        for month in sorted(months):
            insights.append({
                "month": month,
                "top_tracks": top_tracks.get(month, []),
                "top_categories": top_categories.get(month, [])
            })

        return Response(insights)
