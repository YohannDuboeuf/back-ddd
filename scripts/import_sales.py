import sys
import os
import django
import pandas as pd
from tqdm import tqdm

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back_ddd.settings")
django.setup()

from sales_data.models import Product, Sale

def import_sales(csv_path, max_rows=None):
    df = pd.read_csv(csv_path)

    if max_rows:
        df = df.head(max_rows)

    success_count = 0
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Import des ventes"):
        try:
            # Création ou récupération du produit
            product, _ = Product.objects.get_or_create(
                name=row['Description'],
                category=row.get('Category', 'Unknown'),
                defaults={'unit_price': row.get('UnitPrice', 0.0)}
            )

            # Création de la vente
            Sale.objects.create(
                product=product,
                country=row.get('Country', 'Unknown'),
                quantity=int(row['Quantity']) if not pd.isna(row['Quantity']) else 0,
                date=pd.to_datetime(row.get('InvoiceDate', '2023-01-01'))
            )
            success_count += 1

        except Exception as e:
            print(f"❌ Erreur sur la ligne : {e}")

    print(f"\n✅ {success_count} lignes insérées.")

if __name__ == "__main__":
    import_sales("./data/online_sales_dataset.csv")
