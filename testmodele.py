import pandas as pd
import joblib


# Charger le modèle
modele = joblib.load("modele_figures.pkl")

print("Modèle chargé avec succès !")


# Nouvelle figure
nouvelle_figure = pd.DataFrame([{
    "nombre_cotes": 4,
    "cote_a": 8,
    "cote_b": 8,
    "perimetre": 32,
    "surface": 64
}])


# Prédiction
prediction = modele.predict(nouvelle_figure)

print("Figure prédite :", prediction[0])