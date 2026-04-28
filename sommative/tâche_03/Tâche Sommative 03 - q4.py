# 1. Dictionnaire
inventaire = {
    "stylos": 24,
    "cahiers": 15,
    "gommes": 10
}

# 2. Quantité cahiers
print("Cahiers :", inventaire["cahiers"])

# 3. Ajouter marqueurs
inventaire["marqueurs"] = 18

# 4. Modifier stylos
inventaire["stylos"] = 30

# 5. Supprimer gommes
del inventaire["gommes"]

# 6. Affichage
for produit, quantite in inventaire.items():
    print(produit, ":", quantite)

# 7. Total
total = sum(inventaire.values())
print("Total en stock :", total)