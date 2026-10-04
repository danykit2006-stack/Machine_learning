import random as rd
import math as mth
import pandas as pd  



data = []
colonnes = [
    "nombre_cotes",
    "cote_a",
    "cote_b",
    "perimetre",
    "surface",
    "forme_cible"
]
#======================================
#CIRCLE
#======================================
for i in range(500):
    rayon = rd.uniform(1, 20)
    perimetre = 2 * mth.pi * rayon
    surface = mth.pi * rayon ** 2
    data.append((0, rayon, rayon, perimetre, surface, "cercle"))

#======================================
#TRIANGLE
#======================================
for i in range(500):
    cote = rd.uniform(1, 20)
    perimetre = 3 * cote
    surface = (mth.sqrt(3) / 4) * cote ** 2
    data.append((3, cote, cote, perimetre, surface, "triangle"))

#======================================
#SQUARE
#======================================
for i in range(500):
    cote = rd.uniform(1, 20)
    perimetre = 4 * cote
    surface = cote ** 2
    data.append((4, cote, cote, perimetre, surface, "carre"))

#======================================
#RECTANGLE
#======================================
for i in range(500):
    longueur = rd.uniform(1, 20)
    largeur = rd.uniform(1, 20)
    while longueur == largeur:
        largeur = rd.uniform(1, 20)
    perimetre = 2 * (longueur + largeur)
    surface = longueur * largeur
    data.append((4, longueur, largeur, perimetre, surface, "rectangle"))

print(len(data))
df = pd.DataFrame(data, columns=colonnes)
print(df.head())

def randomize_dataframe(df):
    """
    Randomizes the order of the rows in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame to be randomized.

    Returns:
        pd.DataFrame: A new DataFrame with the rows in random order.
    """
    return df.sample(frac=1, random_state=42).reset_index(drop=True)

randomized_df = randomize_dataframe(df)
print(randomized_df.head())
"""
randomized_df.to_csv("dataset.csv", index=False)"""
print(randomized_df.shape)
print(randomized_df["forme_cible"].value_counts())