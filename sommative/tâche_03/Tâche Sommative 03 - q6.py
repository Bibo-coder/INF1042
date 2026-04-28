achats = [
    ("Liam", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Speed Zone", "PlayStation", 49.99),
    ("Liam", "Pixel Quest", "Switch", 39.99),
    ("Noah", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Sky Builder", "PC", 29.99),
    ("Olivia", "Speed Zone", "Xbox", 54.99),
    ("Liam", "Sky Builder", "PC", 29.99),
    ("Noah", "Pixel Quest", "Switch", 39.99)
]

# 1. Affichage
for a in achats:
    print(a)

# 2. Jeux uniques
jeux = {a[1] for a in achats}
print("Jeux :", jeux)

# 3. Plateformes
plateformes = {a[2] for a in achats}
print("Plateformes :", plateformes)

# 4. Total dépensé
total = sum(a[3] for a in achats)
print("Total :", total)

# 5. Dépenses par client
depenses = {}
for nom, jeu, plat, prix in achats:
    depenses[nom] = depenses.get(nom, 0) + prix
print(depenses)

# 6. Client max
max_client = max(depenses, key=depenses.get)
print("Plus dépensé :", max_client)

# 7. Nombre d’achats par jeu
compte_jeux = {}
for a in achats:
    compte_jeux[a[1]] = compte_jeux.get(a[1], 0) + 1
print(compte_jeux)

# 8. Achats PC
print("Achats PC :")
for a in achats:
    if a[2] == "PC":
        print(a)

# 9. Résumé
jeu_plus_achete = max(compte_jeux, key=compte_jeux.get)

print("Résumé :")
print("Nombre d’achats :", len(achats))
print("Jeux uniques :", jeux)
print("Plateformes :", plateformes)
print("Top client :", max_client)
print("Jeu le plus acheté :", jeu_plus_achete)