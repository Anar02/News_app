# 🎵🎮 Music & Gaming News App

Une application Python qui récupère chaque jour les actualités du monde de la musique et des jeux vidéo, en français.

## 🔧 Fonctionnalités

- 📰 Récupération des news via NewsAPI
- 🎮 Actualités gaming
- 🎵 Actualités musicales (à venir)
- 🇫🇷 Contenu filtré en français
- ✅ Prévue pour tourner quotidiennement

## ▶️ Exécution

1. Crée un environnement virtuel :
```bash
python -m venv venv
venv\Scripts\activate  # Sur Windows

2. Installer les requirements :
pip install -r requirements.txt

3. Lancer le projet : 
python main.py

4. Lancer le serveur :
uvicorn main:app --reload