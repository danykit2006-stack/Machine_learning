import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# =========================
# 1. CHARGER LE DATASET
# =========================

df = pd.read_csv("dataset.csv")


# =========================
# 2. DEFINIR X ET y
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
# 6. SAUVEGARDER LE MODELE
# =========================

joblib.dump(modele, "modele_figures.pkl")

print("Modèle sauvegardé avec succès !")


# =========================
# 7. PREDICTIONS
# =========================

y_pred = modele.predict(X_test)


# =========================
# 8. EVALUATION
# =========================

precision = accuracy_score(y_test, y_pred)

print("Précision :", precision)

print("\nRapport de classification :")
print(classification_report(y_test, y_pred))

matrice = confusion_matrix(y_test, y_pred)

affichage = ConfusionMatrixDisplay(
    confusion_matrix=matrice,
    display_labels=modele.classes_
)

affichage.plot()
plt.title("Matrice de confusion")
plt.show()