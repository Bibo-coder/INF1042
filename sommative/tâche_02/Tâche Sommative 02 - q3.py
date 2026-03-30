# Ibrahim Moumneh
# Demander le prix d'achat
prix = float(input("Entrez le prix d'achat ($) : "))

# Déterminer le rabais
if prix < 50:
    rabais = 0
elif prix <= 100:
    rabais = 0.10
else:
    rabais = 0.15

# Calcul du montant du rabais
montant_rabais = prix * rabais

# Sous-total après rabais
sous_total = prix - montant_rabais

# Taxe (exemple : 13%)
taxe = 0.13
montant_taxe = sous_total * taxe

# Total final
total = sous_total + montant_taxe

# Affixhage des résultats
print("--- Facture ---")
print("Prix initial :", prix, "$")
print("Prix appliqué :", rabais * 100, "%")
print("Montant du rabais :", montant_rabais, "$")
print("Sous-total :", sous_total, "$")
print("Taxe :", montant_taxe, "$")
print("Total à payer :", total, "$")