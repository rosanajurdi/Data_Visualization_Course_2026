# Script Python pour analyser le dataset diamonds
# Ce script télécharge, charge et analyse le dataset diamonds.csv

# Étape 1: Importer les bibliothèques nécessaires
import pandas as pd
import seaborn as sns
import numpy as np

# Étape 2: Télécharger et charger le dataset depuis l'URL
url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/diamonds.csv"
diamonds_df = pd.read_csv(url)

# Étape 3: Afficher les 5 premières lignes
print("Les 5 premières lignes du DataFrame :")
print(diamonds_df.head())
print("\n")

# Afficher les 10 premières lignes
print("Les 10 premières lignes du DataFrame :")
print(diamonds_df.head(10))
print("\n")

# Étape 4: Afficher les types de données de chaque colonne
print("Types de données de chaque colonne :")
print(diamonds_df.dtypes)
print("\n")

# Étape 5: Explication des types de variables
# cut, color, clarity = variables catégorielles ordinales (elles ont un ordre hiérarchique)
# carat, depth, table, price, x, y, z = variables continues (valeurs numériques continues)

# Étape 6: Afficher le nombre de lignes et colonnes
print("Nombre de lignes et colonnes :")
print(diamonds_df.shape)
print("\n")

# Étape 7: Générer un résumé statistique
# Pour les valeurs numériques
print("Résumé statistique des valeurs numériques :")
print(diamonds_df.describe())
print("\n")

# Pour les valeurs catégorielles
print("Résumé statistique des valeurs catégorielles :")
print(diamonds_df.describe(include=object))
print("\n")

# Étape 8: Sélectionner des colonnes
# Méthode 1: diamonds_df.cut
print("Sélection de la colonne 'cut' avec diamonds_df.cut :")
print(diamonds_df.cut.head())
print("\n")

# Méthode 2: diamonds_df['cut']
print("Sélection de la colonne 'cut' avec diamonds_df['cut'] :")
print(diamonds_df['cut'].head())
print("\n")

# Étape 9: Créer une nouvelle colonne price_per_carat
diamonds_df['price_per_carat'] = diamonds_df['price'] / diamonds_df['carat']

# Étape 10: Créer une colonne price_per_carat_is_high
diamonds_df['price_per_carat_is_high'] = np.where(diamonds_df['price_per_carat'] > 3500, 1, 0)

# Étape 11: Afficher les 5 premières lignes du DataFrame mis à jour
print("Les 5 premières lignes du DataFrame mis à jour :")
print(diamonds_df.head())
