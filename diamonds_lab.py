# diamonds_lab_complete.py

# ----------------------------------------------
# Lab : Diagrammes à Barres sur les Diamants
# ----------------------------------------------

# Étape 1 : Importer les bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# ----------------------------------------------
# Étape 2 : Charger les données
# ----------------------------------------------
url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/diamonds.csv"
diamonds = pd.read_csv(url)

# Vérifier le chargement
print("5 premières lignes du dataset :")
print(diamonds.head())

# Afficher les types de colonnes
print("\nTypes de colonnes :")
print(diamonds.dtypes)

# ----------------------------------------------
# Étape 3 : Analyse par 'cut'
# ----------------------------------------------
cut_counts = diamonds['cut'].value_counts()
print("\nNombre de diamants par 'cut' :")
print(cut_counts)

# --- Matplotlib ---
plt.figure(figsize=(8,5))
plt.bar(cut_counts.index, cut_counts.values, color='skyblue')
plt.xlabel("Cut")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Cut - Matplotlib")
plt.show()

# --- Seaborn ---
plt.figure(figsize=(8,5))
sns.countplot(data=diamonds, x='cut', palette='pastel')
plt.xlabel("Cut")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Cut - Seaborn")
plt.show()

# --- Plotly ---
cut_counts_df = diamonds['cut'].value_counts().reset_index()
cut_counts_df.columns = ['cut', 'count']
fig_cut_plotly = px.bar(cut_counts_df, x='cut', y='count',
                        labels={'cut':'Cut', 'count':'Nombre de diamants'},
                        title="Nombre de diamants par Cut - Plotly")
fig_cut_plotly.show()
fig_cut_plotly.write_html("graphique_cut_plotly.html")

# --- Altair ---
chart_cut_altair = alt.Chart(cut_counts_df).mark_bar(color='orange').encode(
    x='cut',
    y='count'
).properties(
    title="Nombre de diamants par Cut - Altair"
)
chart_cut_altair.save("graphique_cut_altair.html")

# ----------------------------------------------
# Étape 4 : Analyse par 'color'
# ----------------------------------------------
color_counts = diamonds['color'].value_counts()
print("\nNombre de diamants par 'color' :")
print(color_counts)

# --- Matplotlib ---
plt.figure(figsize=(8,5))
plt.bar(color_counts.index, color_counts.values, color='lightgreen')
plt.xlabel("Color")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Color - Matplotlib")
plt.show()

# --- Seaborn ---
plt.figure(figsize=(8,5))
sns.countplot(data=diamonds, x='color', palette='coolwarm')
plt.xlabel("Color")
plt.ylabel("Nombre de diamants")
plt.title("Nombre de diamants par Color - Seaborn")
plt.show()

# --- Plotly ---
color_counts_df = diamonds['color'].value_counts().reset_index()
color_counts_df.columns = ['color', 'count']
fig_color_plotly = px.bar(color_counts_df, x='color', y='count',
                          labels={'color':'Color', 'count':'Nombre de diamants'},
                          title="Nombre de diamants par Color - Plotly")
fig_color_plotly.show()
fig_color_plotly.write_html("graphique_color_plotly.html")

# --- Altair ---
chart_color_altair = alt.Chart(color_counts_df).mark_bar(color='purple').encode(
    x='color',
    y='count'
).properties(
    title="Nombre de diamants par Color - Altair"
)
chart_color_altair.save("graphique_color_altair.html")

# ----------------------------------------------
# Étape 5 : Prix moyen par 'cut'
# ----------------------------------------------
avg_price_cut = diamonds.groupby('cut')['price'].mean().reset_index()
print("\nPrix moyen par 'cut' :")
print(avg_price_cut)

# --- Matplotlib ---
plt.figure(figsize=(8,5))
plt.bar(avg_price_cut['cut'], avg_price_cut['price'], color='lightcoral')
plt.xlabel("Cut")
plt.ylabel("Prix moyen")
plt.title("Prix moyen par Cut - Matplotlib")
plt.show()

# --- Seaborn ---
plt.figure(figsize=(8,5))
sns.barplot(data=avg_price_cut, x='cut', y='price', palette='magma')
plt.xlabel("Cut")
plt.ylabel("Prix moyen")
plt.title("Prix moyen par Cut - Seaborn")
plt.show()

# --- Plotly ---
fig_price_plotly = px.bar(avg_price_cut, x='cut', y='price',
                          labels={'cut':'Cut', 'price':'Prix moyen'},
                          title="Prix moyen par Cut - Plotly")
fig_price_plotly.show()
fig_price_plotly.write_html("graphique_price_cut_plotly.html")

# --- Altair ---
chart_price_altair = alt.Chart(avg_price_cut).mark_bar(color='teal').encode(
    x='cut',
    y='price'
).properties(
    title="Prix moyen par Cut - Altair"
)
chart_price_altair.save("graphique_price_cut_altair.html")

print("\n✅ Tous les graphiques ont été générés et les fichiers HTML sauvegardés.")