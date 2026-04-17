chemin = "exemples/module4/valeurs.txt"

valeurs = []

# Lecture du fichier
with open(chemin, "r") as fichier:
    for ligne in fichier:
        valeur = int(ligne.strip())
        valeurs.append(valeur)

# Calculs
minimum = min(valeurs)
maximum = max(valeurs)
moyenne = sum(valeurs) / len(valeurs)

# Affichage
print(f"Valeur minimale : {minimum}")
print(f"Valeur maximale : {maximum}")
print(f"Moyenne : {moyenne}")