import sys
import os
import django
import pandas as pd
from tqdm import tqdm  # pour la barre de progression

# Correction du chemin
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back_ddd.settings")
django.setup()

from spotify_data.models import Track
from sales_data.models import Product, Sale

def import_data_from_csv(csv_path, max_rows=None):
    df = pd.read_csv(csv_path)

    if max_rows:
        df = df.head(max_rows)  # Limiter le nombre de lignes

    print(f"Importation de {len(df)} lignes...")

    success_count = 0

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Importation des données"):
        try:
            # Track
            track, _ = Track.objects.get_or_create(
                name=row['name'],
                artist="Unknown",
                defaults={
                    'popularity': row['popularity'],
                    'danceability': row['danceability'],
                    'energy': row['energy'],
                    'valence': 0.0,
                    'tempo': 120.0,
                    'country': row['country']
                }
            )

            # Product
            product, _ = Product.objects.get_or_create(
                name=row['name'],
                category=row['Category'],
                defaults={
                    'unit_price': row['UnitPrice'] if not pd.isna(row['UnitPrice']) else 0.0
                }
            )

            # Sale
            Sale.objects.create(
                product=product,
                country=row['country'],
                quantity=int(row['Quantity']),
                date=pd.to_datetime("2023-01-01")
            )

            success_count += 1

        except Exception as e:
            print(f"Erreur sur la ligne {row}: {e}")

    print(f"\n✅ Import terminé : {success_count} lignes insérées avec succès.")

if __name__ == "__main__":
    import_data_from_csv("./data/donnees_traite.csv", max_rows=5000)