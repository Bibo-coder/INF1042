# 1. Tuple produit
produit = ("Clavier", 49.99, 12)

# 2. Affichage séparé
print(produit[0], produit[1], produit[2])

# 3. Déballage
nom, prix, quantite = produit

# 4. Phrase
print(f"Le produit {nom} coûte {prix} $ et il y en a {quantite} en stock.")

# 5. Deuxième produit
produit2 = ("Souris", 29.99, 20)

# Comparaison
if produit[1] > produit2[1]:
    print("Le produit le plus cher est :", produit[0])
else:
    print("Le produit le plus cher est :", produit2[0])