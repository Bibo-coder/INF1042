import random
import string

# Demander les informations à l'utilisateur
prenom = input("Entrez votre prénom : ").lower()
nom = input("Entrez votre nom : ").lower()
annee_naissance = int(input("Entrez votre année de naissance : "))
ville = input("Entrez votre ville : ").lower()

# Création du nom d'utilisateur
nom_utilisateur = f"{prenom}.{nom}"
identifiant_complet = f"{prenom}.{nom}@{ville}.ca"

# Vérification de l'âge
from datetime import datetime
annee_courante = datetime.now().year
age = annee_courante - annee_naissance

if age >= 18:
    majeur = True
    print("L'utilisateur a 18 ans ou plus")
else:
    majeur = False
    print("L'utilisateur a moins de 18 ans")

# Création d'un mot de passe simple
lettres_alea = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
mot_de_passe = prenom[:2] + nom[-2:] + str(annee_naissance) + lettres_alea

# Affichage
print("\n--- Résultats ---")
print(f"Nom d'utilisateur : {nom_utilisateur}")
print(f"Identifiant complet : {identifiant_complet}")
print(f"Mot de passe : {mot_de_passe}")