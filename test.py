from pydantic import BaseModel  # Utilisé pour la validation des données
import numpy as np
import pandas as pd  # Utilisé pour la manipulation de données
import joblib  # Utilisé pour charger le modèle sauvegardé
from flask import Flask, request, jsonify  # Flask est un micro-framework pour les applications web
# Charger le modèle  depuis le disque
modele = joblib.load('modeladaboost.pkl')

# Définition du schéma des données d'entrée avec Pydantic
# Cela garantit que les données reçues correspondent aux attentes du modèle
class DonneesEntree(BaseModel):
    delais_1_signe_adm_hop :int
    delais_adm_hop_prise_charge : int
    Suivi_tempsdeSuiviaprèstraitement : int
    enc_antecedent_HTA : int
    enc_antecedent_diabete : int
    enc_antecedent_cardiopathie : int
    enc_clinique_hémiplégie : int
    enc_clinique_Aphasie : int
    enc_clinique_Paralysie_faciale : int
    enc_clinique_Hémiparésie : int
    enc_SV_Engagement_Cerebral : int
    enc_SV_inondation_Ventriculaire : int
    enc_id_sexe : int
    enc_Traitement : int

# Création de l'instance de l'application Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def accueil():
    return jsonify({"Message": "Bienvenue sur l'API de predictionde decces suite a l'AVC"})
@app.route("/predire", methods=['POST'])
def predire():
    if not request.json:
        return jsonify({"erreur": "Aucun JSON fourni"}), 400
    try:
        # Extraction et validation des données d'entrée en utilisant Pydantic
        donnees = DonneesEntree(**request.json)
        donnees_df = pd.DataFrame([donnees.dict()])  # Conversion en DataFrame

        # Utilisation du modèle pour prédire et obtenir les probabilités
        predictions = modele.predict(donnees_df)
        probabilities = modele.predict_proba(donnees_df)[:, 1]  # Probabilité de la classe positive (diabète)

        # Compilation des résultats dans un dictionnaire
        resultats = donnees.dict()
        resultats['prediction'] = int(predictions[0])
        resultats['probabilite_survie'] = probabilities[0]

        # Renvoie les résultats sous forme de JSON
        return jsonify({"resultats": resultats})
    except Exception as e:
        # Gestion des erreurs et renvoi d'une réponse d'erreur
        return jsonify({"erreur": str(e)}), 400

# Point d'entrée pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Lancement de l'application sur le port 8000 avec le mode debug activé