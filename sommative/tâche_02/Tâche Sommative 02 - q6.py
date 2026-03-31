# Ibrahim Moumneh
# Demander les informations
heures = float(input("Entrez le nombre d'heures stationnées : "))
electrique = input("La voiture est-elle électrique ? (oui/non) : ").lower()

# Calcul du coût de base
if heures <= 1:
    cout = 4
else:
    cout = 4 + (heures - 1) * 3

# Frais fixt si plus de 5 heures
if heures > 5:
    cout += 10

# Rabais pour voiture électrique (20%)
if electrique == "oui":
    cout *= 0.8  # Enlève 20%

# Affichage du résultat
print("Cout total du stationnement :", round(cout, 2), "$")