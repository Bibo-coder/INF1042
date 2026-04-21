# 1) Création du dictionnaire élève
eleve = {
    "nom": "Alex",
    "age": 16,
    "programme": "Sciences"
}

# Dictionnaire donné
notes = {"math": 78, "Français": 85, "science": 91}

# 2) Afficher la note de science
print(notes["science"])

# 3) Ajouter "histoire" et modifier "math"
notes["histoire"] = 88
notes["math"] = 82

# 4) Boucle for pour afficher les matières et notes
for matiere, note in notes.items():
    print(f"Matière: {matiere} | Note: {note}")

# 5) Compter les occurrences des mots
mots = ["chat", "chien", "chat", "oiseau", "chien", "chat"]

compte = {}

for mot in mots:
    if mot in compte:
        compte[mot] += 1
    else:
        compte[mot] = 1

print(compte)