# ----------------------------------------------
# Lab : Diagrammes à Barres sur les Diamants
# ----------------------------------------------

# Étape 1 : Importer les bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# Étape 2 : Charger les données
url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/diamonds.csv"
diamonds = pd.read_csv(url)

# Vérifier que ça marche
print("5 premières lignes du dataset :")
print(diamonds.head())

# Afficher les types de colonnes
print("\nTypes de colonnes :")
print(diamonds.dtypes)

# Étape 3 : Compter le nombre de diamants par 'cut'
cut_counts = diamonds['cut'].value_counts()
print("\nNombre de diamants par 'cut' :")
print(cut_counts)

# ----------------------------------------------
# Étape 4 : Diagramme à barres avec Matplotlib
# ----------------------------------------------
plt.figure(figsize=(8,5))
plt.bar(cut_counts.index, cut_counts.values, color='skyblue')
plt.xlabel("Cut")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Cut - Matplotlib")
plt.show()

# ----------------------------------------------
# Étape 5 : Diagramme à barres avec Seaborn
# ----------------------------------------------
plt.figure(figsize=(8,5))
sns.countplot(data=diamonds, x='cut', palette='pastel')
plt.xlabel("Cut")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Cut - Seaborn")
plt.show()

# ----------------------------------------------
# Étape 6 : Diagramme à barres interactif avec Plotly
# ----------------------------------------------
cut_counts_df = diamonds['cut'].value_counts().reset_index()
cut_counts_df.columns = ['cut', 'count']

fig = px.bar(cut_counts_df, x='cut', y='count',
             labels={'cut':'Cut', 'count':'Nombre de diamants'},
             title="Nombre de diamants par Cut - Plotly")
fig.show()  # peut ne rien afficher dans .py
fig.write_html("graphique_cut_plotly.html")  # ouvre ce fichier dans le navigateur

# ----------------------------------------------
# Étape 7 : Diagramme à barres avec Altair
# ----------------------------------------------
chart = alt.Chart(cut_counts_df).mark_bar(color='orange').encode(
    x='cut',
    y='count'
).properties(
    title="Nombre de diamants par Cut - Altair"
)

# Altair peut être affiché dans un notebook, sinon on exporte en HTML
chart.save("graphique_cut_altair.html")
print("\nLes graphiques interactifs Plotly et Altair ont été créés en HTML dans le dossier du projet.")

# Compter le nombre de diamants par 'color'
color_counts = diamonds['color'].value_counts()
print("\nNombre de diamants par 'color' :")
print(color_counts)

# Diagramme Matplotlib
plt.figure(figsize=(8,5))
plt.bar(color_counts.index, color_counts.values, color='lightgreen')
plt.xlabel("Color")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Color - Matplotlib")
plt.show()

# Diagramme Seaborn
plt.figure(figsize=(8,5))
sns.countplot(data=diamonds, x='color', palette='coolwarm')
plt.xlabel("Color")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Color - Seaborn")
plt.show()

# Prix moyen par 'cut'
avg_price_cut = diamonds.groupby('cut')['price'].mean().reset_index()
print("\nPrix moyen par 'cut' :")
print(avg_price_cut)

# Diagramme Seaborn
plt.figure(figsize=(8,5))
sns.barplot(data=avg_price_cut, x='cut', y='price', palette='magma')
plt.xlabel("Cut")
plt.ylabel("Prix moyen")
plt.title("Prix moyen des diamants par Cut - Seaborn")
plt.show()


fig = px.bar(avg_price_cut, x='cut', y='price',
             labels={'cut':'Cut', 'price':'Prix moyen'},
             title="Prix moyen des diamants par Cut - Plotly")
fig.write_html("prix_moyen_cut_plotly.html")
chart = alt.Chart(avg_price_cut).mark_bar(color='purple').encode(
    x='cut',
    y='price'
).properties(title="Prix moyen des diamants par Cut - Altair")
chart.save("prix_moyen_cut_altair.html")