# GéoForme

Application Flask de classification de figures géométriques et de visualisation 3D.

## Lancer en local

Avec Python 3.14 et les dépendances déclarées :

```bash
python -m pip install -r requirements.txt
python app.py
```

Ouvrez ensuite <http://127.0.0.1:5000>.

## Déployer sur Vercel

1. Importez le dépôt dans Vercel en conservant la racine du projet comme **Root Directory**.
2. Vercel détecte l’application Flask dans `app.py`, installe les paquets de `requirements.txt` et sélectionne Python 3.14 grâce à `.python-version`.
3. Déployez le projet. Le fichier `vercel.json` inclut explicitement le modèle et le dossier `frontend/` dans la Function.

L’interface est dans `frontend/`; l’endpoint JSON `POST /predict` et la page d’accueil sont servis par Flask.
