import sys
import os
import django
import pandas as pd
from tqdm import tqdm

# Setup Django
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back_ddd.settings")
django.setup()

from spotify_data.models import Track

def import_additional_tracks(csv_path, max_rows=None):
    df = pd.read_csv(csv_path)

    if max_rows:
        df = df.head(max_rows)

    print(f"Importation de {len(df)} lignes...")

    success_count = 0

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Ajout des nouveaux tracks"):
        try:
            existing_track = Track.objects.filter(
                name=row['name'],
                country=row['country'],
                date=row['snapshot_date']
            ).first()

            if existing_track:
                if existing_track.artist == "Unknown":
                    # Mise à jour de l'artiste si vide
                    existing_track.artist = row['artists']
                    existing_track.popularity = row.get('popularity', existing_track.popularity)
                    existing_track.danceability = row.get('danceability', existing_track.danceability)
                    existing_track.energy = row.get('energy', existing_track.energy)
                    existing_track.valence = row.get('valence', existing_track.valence)
                    existing_track.tempo = row.get('tempo', existing_track.tempo)
                    existing_track.save()
                    existing_track.date = row['snapshot_date']
                    success_count += 1
                if existing_track.date == "-":
                    # Mise à jour de l'artiste si vide
                    existing_track.artist = row['artists']
                    existing_track.popularity = row.get('popularity', existing_track.popularity)
                    existing_track.danceability = row.get('danceability', existing_track.danceability)
                    existing_track.energy = row.get('energy', existing_track.energy)
                    existing_track.valence = row.get('valence', existing_track.valence)
                    existing_track.tempo = row.get('tempo', existing_track.tempo)
                    existing_track.save()
                    existing_track.date = row['snapshot_date']
                    success_count += 1
            else:
                # Créer un nouveau track si aucun trouvé
                Track.objects.create(
                    name=row['name'],
                    artist=row['artists'],
                    popularity=row.get('popularity', 0.0),
                    danceability=row.get('danceability', 0.0),
                    energy=row.get('energy', 0.0),
                    valence=row.get('valence', 0.0),
                    tempo=row.get('tempo', 120.0),
                    country=row['country'],
                    date=row['snapshot_date'],
                )
                success_count += 1

                success_count += 1

        except Exception as e:
            print(f"Erreur sur la ligne {row}: {e}")

    print(f"\n✅ Import terminé : {success_count} nouveaux tracks ajoutés sans doublons.")

if __name__ == "__main__":
    import_additional_tracks("./data/all_track.csv")
