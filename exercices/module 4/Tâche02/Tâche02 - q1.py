import random
import os

# Chemin du fichier
chemin = "exemples/module4/valeurs.txt"

# Créer les dossiers si nécessaire
os.makedirs(os.path.dirname(chemin), exist_ok=True)

# Écriture des 1000 valeurs aléatoires
with open(chemin, "w") as fichier:
    for _ in range(1000):
        valeur = random.randint(0, 100000)
        fichier.write(str(valeur) + "\n")

print("Fichier créé avec succès !")