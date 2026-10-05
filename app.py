from math import cos, pi, sin
from pathlib import Path

from flask import Flask, jsonify, render_template, request
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR),
    static_folder=str(BASE_DIR / "static"),
)

modele = joblib.load(BASE_DIR / "modele_figures.pkl")

COLONNES = ["nombre_cotes", "cote_a", "cote_b", "perimetre", "surface"]


def creer_geometrie(forme: str, cote_a: float, cote_b: float, surface: float) -> dict:
    """Construit les sommets normalisés de la forme à extruder dans le navigateur."""
    if forme == "cercle":
        points = [
            [cos(2 * pi * index / 48), sin(2 * pi * index / 48)]
            for index in range(48)
        ]
    elif forme == "triangle":
        points = [[-1, -0.58], [1, -0.58], [0, 1.15]]
    elif forme == "rectangle":
        rapport = cote_b / cote_a
        demi_hauteur = max(0.35, min(1.5, rapport))
        points = [
            [-1, -demi_hauteur],
            [1, -demi_hauteur],
            [1, demi_hauteur],
            [-1, demi_hauteur],
        ]
    else:
        points = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

    return {
        "points": points,
        "profondeur": 0.42,
        "surface": surface,
    }


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    donnees = request.get_json(silent=True)
    if not isinstance(donnees, dict):
        return jsonify({"erreur": "Les données reçues doivent être au format JSON."}), 400

    valeurs = {}
    for colonne in COLONNES:
        valeur = donnees.get(colonne)
        if isinstance(valeur, bool) or not isinstance(valeur, (int, float)):
            return jsonify({"erreur": f"Le champ « {colonne} » doit être un nombre."}), 400
        if not pd.notna(valeur) or not float("-inf") < valeur < float("inf"):
            return jsonify({"erreur": f"Le champ « {colonne} » doit être un nombre fini."}), 400
        valeurs[colonne] = float(valeur)

    if valeurs["nombre_cotes"] < 0 or not valeurs["nombre_cotes"].is_integer():
        return jsonify({"erreur": "Le nombre de côtés doit être un entier positif ou nul."}), 400
    if any(valeurs[nom] <= 0 for nom in ("cote_a", "cote_b", "perimetre", "surface")):
        return jsonify({"erreur": "Les côtés, le périmètre et la surface doivent être supérieurs à zéro."}), 400

    figure = pd.DataFrame([[valeurs[colonne] for colonne in COLONNES]], columns=COLONNES)
    forme = str(modele.predict(figure)[0])
    geometrie = creer_geometrie(
        forme,
        valeurs["cote_a"],
        valeurs["cote_b"],
        valeurs["surface"],
    )

    return jsonify({"forme": forme, "geometrie": geometrie})


if __name__ == "__main__":
    app.run(debug=True)
