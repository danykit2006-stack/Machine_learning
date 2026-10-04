import random
import math

#Data generation for the circle geometry figure
for i in range(5):

    rayon = random.uniform(1, 20)

    perimetre = 2 * math.pi * rayon
    surface = math.pi * rayon ** 2

    print(
        0,
        rayon,
        rayon,
        perimetre,
        surface,
        "cercle"
    )

#Data generation for the triangle geometry figure
for i in range(5):

    cote = random.uniform(1, 20)

    perimetre = 3 * cote
    surface = (math.sqrt(3) / 4) * cote ** 2

    print(
        3,
        cote,
        cote,
        perimetre,
        surface,
        "triangle"
    ) 


#Data generation for the square geometry figure
for i in range(5):

    cote = random.uniform(1, 20)

    perimetre = 4 * cote
    surface = cote ** 2

    print(
        4,
        cote,
        cote,
        perimetre,
        surface,
        "carre"
    )       

#Data generation for the rectangle geometry figure
for i in range(5):

    longueur = random.uniform(1, 20)
    largeur = random.uniform(1, 20)

    while longueur == largeur:
        largeur = random.uniform(1, 20)

    perimetre = 2 * (longueur + largeur)
    surface = longueur * largeur

    print(
        4,
        longueur,
        largeur,
        perimetre,
        surface,
        "rectangle"
    )    