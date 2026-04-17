panier = ["pomme", "banane", "orange", "banane"]

# Insérer "kiwi" à l’index 1
panier.insert(1, "kiwi")

# Retirer "banane" (la première occurrence)
panier.remove("banane")

# Retirer et récupérer le dernier élément
dernier = panier.pop()

# Affichage
print("Panier :", panier)
print("Dernier :", dernier)