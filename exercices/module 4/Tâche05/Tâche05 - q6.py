matchs = (
("Tigres", "Lynx", 25, 18),
("Aigles", "Panthères", 22, 25),
("Tigres", "Panthères", 25, 23),
("Lynx", "Aigles", 19, 25),
("Tigres", "Aigles", 21, 25),
("Lynx", "Panthères", 25, 20)
)

victoires = {}
defaites = {}
points = {}

for m in matchs:
    e1, e2, s1, s2 = m

    victoires.setdefault(e1, 0)
    victoires.setdefault(e2, 0)
    defaites.setdefault(e1, 0)
    defaites.setdefault(e2, 0)
    points.setdefault(e1, 0)
    points.setdefault(e2, 0)

    points[e1] += s1
    points[e2] += s2

    if s1 > s2:
        gagnant, perdant = e1, e2
        victoires[e1] += 1
        defaites[e2] += 1
    else:
        gagnant, perdant = e2, e1
        victoires[e2] += 1
        defaites[e1] += 1

    print(f"Les {gagnant} ont battu les {perdant} par {max(s1, s2)} à {min(s1, s2)}.")

print("\nVictoires :", victoires)
print("Points :", points)

# Meilleure équipe (victoires)
meilleure_victoires = max(victoires, key=victoires.get)
print("\nÉquipe avec le plus de victoires :", meilleure_victoires)

# Meilleure équipe (points)
meilleur_points = max(points, key=points.get)
print("Équipe avec le plus de points :", meilleur_points)

# Analyse victoires / défaites
print("\nAnalyse victoires/défaites :")
for equipe in victoires:
    v = victoires[equipe]
    d = defaites[equipe]

    if v > d:
        etat = "plus de victoires que de défaites"
    elif v == d:
        etat = "autant de victoires que de défaites"
    else:
        etat = "plus de défaites que de victoires"

    print(f"{equipe} : {etat}")