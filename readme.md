# 🎵🛒 Cross-Analytics - Application d’analyse Spotify & E-Commerce (TP 2025)

Ce projet Django + Vue.js propose une plateforme d’analyse croisée entre les données musicales issues de Spotify et des données de ventes e-commerce multi-pays. Il permet de produire des recommandations musicales contextualisées, d’identifier des corrélations entre préférences musicales et comportements d’achat, et de visualiser les tendances via des outils statistiques (PCA, KMeans, etc.).

---

## 🧱 Identification des Bounded Contexts

| Contexte                     | Description                                                                     |
|------------------------------|---------------------------------------------------------------------------------|
| 🎶 **Spotify Analytics**     | Gestion des morceaux, artistes, métriques (popularité, danceability, energy...) |
| 🛒 **E-Commerce**            | Données de vente : produit, pays, catégorie, quantité vendue                    |
| 📊 **Analytics**             | Services d’analyse : clustering KMeans, corrélation, ACP                        |
| 🖥 **Interface & Reporting** | Visualisation des analyses et interactions utilisateur via Vue.js               |

---

## 🗣️ Ubiquitous Language

| Terme                | Signification                                         |
|----------------------|-------------------------------------------------------|
| `Track`              | Morceau issu de Spotify                               |
| `Sale`               | Vente d’un produit                                    |
| `Cluster`            | Groupe de morceaux similaires                         |
| `Correlation Circle` | Visualisation des relations entre variables musicales |
| `PCA`                | Analyse en Composantes Principales                    |
| `Country`            | Pays d’achat                                          |
| `Category`           | Catégorie de produit                                  |
| `Quantity`           | Nombre d’unités vendues                               |
| `UnitPrice`          | Prix unitaire                                         |

---

## 🧠 Modélisation du Domaine

### 🔗 Bounded Contexts et Agrégats

#### `spotify_data`
- **Entité racine** : `Track`
- **Objets valeur** : `Popularity`, `Danceability`, `Energy`
- **Rôle** : Représente un morceau avec ses caractéristiques musicales

#### `sales_data`
- **Entité racine** : `Sale`
- **Objets valeur** : `Country`, `Category`, `UnitPrice`
- **Rôle** : Représente une vente enregistrée dans un pays donné

#### `analytics`
- **Entité racine** : `Cluster`
- **Associations** : avec `Track`
- **Rôle** : Représente un groupe de morceaux similaires selon clustering KMeans et analyse PCA

---

## 🔁 Context Mapping

```plaintext
+----------------------+        +-------------------+
| Spotify Analytics    |<----->|    Analytics       |
| (spotify_data)       |        | (analytics)        |
+----------------------+        +-------------------+
           |                              |
           v                              v
+----------------------+        +-------------------+
|  E-Commerce          |<------>| Interface &       |
|  (sales_data)        |        | Reporting (Vue.js)|
+----------------------+        +-------------------+

```

## Structure du projet

data_platform/
├── spotify_data/          # Données issues de Spotify
├── sales_data/            # Données de ventes
├── recommentation/        # Résultats d'analyse et recommandations
├── analytics/             # Services d’analyse (clustering, ACP, corrélation)
├── back_ddd/              # Fichiers de configuration Django
├── script/                # Scripts d’import de données CSV
├── data/                  # Fichiers sources CSV (Spotify, ventes)
└── manage.py              # Point d’entrée Django

## 📡 Routes API Disponibles

### 🔐 Authentification & Utilisateurs (`/users/`)

| Méthode | Route                          | Description                                       |
|---------|--------------------------------|---------------------------------------------------|
| `POST`  | `/users/login/`                | Connexion (retourne un JWT)                      |
| `POST`  | `/users/register/`             | Inscription d’un nouvel utilisateur              |
| `POST`  | `/users/token/refresh/`        | Rafraîchissement du token JWT                    |
| `GET`   | `/users/all/`                  | Liste de tous les utilisateurs                   |
| `GET`   | `/users/<user_id>/`            | Détail d’un utilisateur                          |
| `POST`  | `/users/create/`               | Création manuelle d’un utilisateur               |
| `DELETE`| `/users/<user_id>/delete/`     | Suppression d’un utilisateur                     |
| `PUT`   | `/users/<user_id>/update/`     | Mise à jour des infos d’un utilisateur           |

---

### 🎵 Données Spotify (`/api/`)

| Méthode | Route                                     | Description                                        |
|---------|-------------------------------------------|----------------------------------------------------|
| `GET`   | `/api/tracks/`                            | Liste des morceaux Spotify avec toutes les métriques |
| `GET`   | `/api/tracks/country/<country>/`          | Morceaux disponibles dans un pays donné            |
| `GET`   | `/api/tracks/top/<country>/`              | Morceaux les plus populaires dans un pays donné    |

---

### 🛒 Données E-commerce (`/api/`)

| Méthode | Route                                     | Description                                        |
|---------|-------------------------------------------|----------------------------------------------------|
| `GET`   | `/api/products/`                          | Liste des produits disponibles                     |
| `GET`   | `/api/sales/`                             | Liste complète des ventes                         |
| `GET`   | `/api/sales/country/<country>/`           | Ventes par pays                                    |
| `GET`   | `/api/sales/top/<country>/`               | Produits les plus vendus dans un pays donné        |

---

### 📊 Recommandation et Analytique (`/api/`)

| Méthode | Route                                     | Description                                        |
|---------|-------------------------------------------|----------------------------------------------------|
| `GET`   | `/api/insights/<countr## 📡 Routes API Disponibles

| Méthode | Route                             | Description                                                          |
|---------|-----------------------------------|----------------------------------------------------------------------|
| `GET`   | `/api/tracks/`                    | Liste des morceaux avec toutes les métriques musicales              |
| `GET`   | `/api/tracks/<id>/`               | Détail d’un morceau spécifique                                      |
| `GET`   | `/api/sales/`                     | Liste des ventes e-commerce (produit, pays, quantité, prix)         |
| `POST`  | `/api/analytics/clusters/`        | Calcule les clusters de morceaux via KMeans                         |
| `GET`   | `/api/analytics/correlation/`     | Renvoie les résultats de la corrélation entre variables musicales   |
| `GET`   | `/api/analytics/pca/`             | Projection ACP (PCA) des morceaux pour visualisation                |
| `POST`  | `/api/recommendations/`           | Génère des recommandations musicales selon des critères utilisateur |
y>/`                | Recommandations ou insights pour un pays donné     |


## Workflow d’utilisation

1. **Chargement des données**
   - Les fichiers CSV (issues de Spotify et du e-commerce) doivent être déposé chargés dans les répertoires appropriés (`data/`).
   - Des scripts ETL (dans le dossier `script/`) lisent, nettoient et préparent ces données.
   - Execution des fichiers ETL

2. **Importation en base**
   - Les données traitées sont insérées dans la base SQLite à l’aide des modèles Django (`Track`, `Sale`, etc.).

3. **Analyse des données**
   - Le backend déclenche plusieurs traitements analytiques :
   - **Corrélation** entre les métriques musicales et les données de vente.
   - **Détermination du nombre optimal de clusters** via la méthode du coude.
   - **Application de l’algorithme KMeans** pour grouper les morceaux similaires.
   - **Projection ACP (PCA)** pour visualiser la structure des données.

4. **Exposition via API**
   - Toutes les données et résultats sont exposés via une API REST (Django REST Framework).
   - Ces routes sont consommées par l’interface Vue.js.

5. **Visualisation et Interaction**
   - L'utilisateur interagit avec le frontend Vue.js pour :
   - Visualiser les clusters et cercles de corrélation.
   - Obtenir des recommandations personnalisées.
   - Analyser les ventes par pays/catégorie.

6. **Évolution & Extension**
   - Le système peut être enrichi avec :
   - De nouveaux types d’analyses (e.g. séries temporelles).
   - L’ajout d’un profil utilisateur.
   - L’authentification sécurisée et la personnalisation des recommandations.
