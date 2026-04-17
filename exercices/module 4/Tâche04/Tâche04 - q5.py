grille = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

sommes = []

for ligne in grille:
    total = 0
    for valeur in ligne:
        total += valeur
    sommes.append(total)

print(sommes)