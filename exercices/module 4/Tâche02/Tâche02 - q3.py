import os

chemin_entree = "exemples/module4/valeurs.txt"
chemin_bas = "exemples/module4/bas.txt"
chemin_haut = "exemples/module4/haut.txt"

# S'assurer que le dossier existe
os.makedirs(os.path.dirname(chemin_entree), exist_ok=True)

with open(chemin_entree, "r") as fichier_entree, \
     open(chemin_bas, "w") as fichier_bas, \
     open(chemin_haut, "w") as fichier_haut:

    for ligne in fichier_entree:
        valeur = int(ligne.strip())

        if valeur <= 49999:
            fichier_bas.write(str(valeur) + "\n")
        else:
            fichier_haut.write(str(valeur) + "\n")

print("Fichiers 'bas.txt' et 'haut.txt' créés avec succès !")