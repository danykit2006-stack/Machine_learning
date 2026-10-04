import random as rd
import math as mth
import pandas as pd
data = []

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