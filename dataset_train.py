import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# =========================
# 1. CHARGER LE DATASET
# =========================

df = pd.read_csv("dataset.csv")


# =========================
# 2. X ET y
# =========================

X = df[
    [
        "nombre_cotes",
        "cote_a",
        "cote_b",
        "perimetre",
        "surface"
    ]
]

y = df["forme_cible"]


# =========================
# 3. TRAIN / TEST
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# =========================
# 4. CREER LE MODELE
# =========================

modele = DecisionTreeClassifier(
    random_state=42
)


# =========================
# 5. ENTRAINEMENT
# =========================

modele.fit(X_train, y_train)


# =========================
# 6. PREDICTIONS
# =========================

y_pred = modele.predict(X_test)


# =========================
# 7. EVALUATION
# =========================

precision = accuracy_score(y_test, y_pred)

print("Précision :", precision)

print("\nRapport de classification :")
print(classification_report(y_test, y_pred))


# =========================
# 8. TEST PERSONNEL
# =========================

figure = [[
    4,      # nombre de côtés
    8,      # cote_a
    8,      # cote_b
    32,     # périmètre
    64      # surface
]]

prediction = modele.predict(figure)

print("\nFigure prédite :", prediction[0])