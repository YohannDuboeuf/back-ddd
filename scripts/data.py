import os
import django
import pandas as pd

from spotify_data.models import Track
from sales_data.models import Product, Sale

django.setup()


def import_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        # Enregistrement du morceau
        track, _ = Track.objects.get_or_create(
            name=row['name'],
            artist="Unknown",
            defaults={
                'popularity': row['popularity'],
                'danceability': row['danceability'],
                'energy': row['energy'],
                'valence': 0.0,
                'tempo': 120.0,
            }
        )

        product, _ = Product.objects.get_or_create(
            name=row['name'],
            category=row['Category'],
            defaults={'unit_price': row['UnitPrice']}
        )

        Sale.objects.create(
            product=product,
            country=row['Country'],
            quantity=row['Quantity'],
            date=pd.to_datetime("2025-01-01")
        )

if __name__ == "__main__":
    import_data_from_csv("../data/donnees_traite.csv")