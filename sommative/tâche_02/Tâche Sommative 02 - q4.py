# Ibrahim Moumneh
import random

# Demander combien de valeurs générer
nb = int(input("Combien de valeurs voulez-vous simuler ? "))

# Compteurs pour chaque valeur
compte_1 = 0
compte_2 = 0
compte_3 = 0
compte_4 = 0

# Générations des nombres aléatoires
for i in range(nb):
    valeur = random.randint(1, 4)

    if valeur == 1:
        compte_1 += 1
    elif valeur == 2:
        compte_2 += 1
    elif valeur == 3:
        compte_3 += 1
    else:
        compte_4 += 1

# Calcul des pourcentages
pourc_1 = (compte_1 / nb) * 100
pourc_2 = (compte_2 / nb) * 100
pourc_3 = (compte_3 / nb) * 100
pourc_4 = (compte_4 / nb) * 100

# Affichage des résultats
print("--- Résultats ---")
print(f"Valeur 1 : {compte_1} fois ({pourc_1:.1f} %)")
print(f"Valeur 2 : {compte_2} fois ({pourc_2:.1f} %)")
print(f"Valeur 3 : {compte_3} fois ({pourc_3:.1f} %)")
print(f"Valeur 4 : {compte_4} fois ({pourc_4:.1f} %)")