import requests

# URL de base de l'API
url_base = 'http://127.0.0.1:8000'

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)
# Données d'exemple pour la prédiction
donnees_predire = {
    "Suivi_tempsdeSuiviaprèstraitement" : 30,
    "delais_1_signe_adm_hop" :140,
    "delais_adm_hop_prise_charge" : 220,
    "enc_antecedent_HTA" : 0,
    "enc_antecedent_diabete" : 1,
    "enc_antecedent_cardiopathie" : 0,
    "enc_clinique_hémiplégie" : 1,
    "enc_clinique_Aphasie" : 0,
    "enc_clinique_Paralysie_faciale" : 1,
    "enc_clinique_Hémiparésie" : 0,
    "enc_SV_Engagement_Cerebral" : 1,
    "enc_SV_inondation_Ventriculaire" : 0,
    "enc_id_sexe": 0,
    "enc_Traitement" : 2
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)


# Données d'exemple pour la prédiction avec haute probabilité de diabète
donnees_predire_haute_proba_diabete = {
    "Suivi_tempsdeSuiviaprèstraitement" : 60,
    "delais_1_signe_adm_hop" :230,
    "delais_adm_hop_prise_charge" : 120,
    "enc_antecedent_HTA" : 1,
    "enc_antecedent_diabete" : 1,
    "enc_antecedent_cardiopathie" : 1,
    "enc_clinique_hémiplégie" : 0,
    "enc_clinique_Aphasie" : 1,
    "enc_clinique_Paralysie_faciale" : 0,
    "enc_clinique_Hémiparésie" : 0,
    "enc_SV_Engagement_Cerebral" : 0,
    "enc_SV_inondation_Ventriculaire" : 1,
    "enc_id_sexe": 0,
    "enc_Traitement" : 1
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire_haute_proba_diabete)
print("Réponse du endpoint de prédiction:", response.text)