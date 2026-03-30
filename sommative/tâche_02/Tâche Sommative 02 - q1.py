# Ibrahim Moumneh
# Nombre de mois dans une année
mois = 12

# Année non-bissextile
jours_non_bissextile = 365
moyenne_non_bissextile = jours_non_bissextile / mois

# Année bissextile
jours_bissextile = 366
moyenne_bissextile = jours_bissextile / mois

# Affichage des résultats
print("Année non-bissextile :")
print("Nombre moyen de jours par mois =", moyenne_non_bissextile)

print("Année bissextile :")
print("Nombre moyen de jours par mois =", moyenne_bissextile)