eleves = [
    {"nom": "Ava", "niveau": 12, "activites": ["programmation", "robotique", "mathématiques"]},
    {"nom": "Liam", "niveau": 11, "activites": ["robotique", "sport"]},
    {"nom": "Emma", "niveau": 12, "activites": ["musique", "mathématiques"]},
    {"nom": "Noah", "niveau": 10, "activites": ["programmation"]}
]

# 1. Noms
for e in eleves:
    print(e["nom"])

# 2. Niveau 12
print("Niveau 12 :")
for e in eleves:
    if e["niveau"] == 12:
        print(e["nom"])

# 3. Activités uniques
activites = set()
for e in eleves:
    activites.update(e["activites"])
print("Activités :", activites)

# 4. Plus d'activités
max_eleve = max(eleves, key=lambda e: len(e["activites"]))
print("Plus actif :", max_eleve["nom"])

# 5. Robotique
count = sum(1 for e in eleves if "robotique" in e["activites"])
print("Participants robotique :", count)