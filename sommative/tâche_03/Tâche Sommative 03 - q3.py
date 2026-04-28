liste_a = ["Batterie", "Basse", "Piano", "Basse", "Guitare", "Batterie"]
liste_b = ["Piano", "Voix", "Guitare", "Synthé", "Piano"]

# 1. Conversion en ensembles
set_a = set(liste_a)
set_b = set(liste_b)

# 2. Chansons uniques
print("Liste A :", set_a)
print("Liste B :", set_b)

# 3. Communes
print("Communes :", set_a & set_b)

# 4. Dans une seule liste
print("Différentes :", set_a ^ set_b)

# 5. Toutes uniques
print("Toutes :", set_a | set_b)