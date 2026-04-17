phrase = "Le petit ordinateur triste oublia ses rêves et pleura dans le silence."

# Transformer la phrase en liste de mots
mots = phrase.split()

# Inverser l'ordre des mots
inverse = mots[::-1]

# Affichage
print(" ".join(inverse))