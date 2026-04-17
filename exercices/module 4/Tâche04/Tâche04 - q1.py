notes = [12, 15, 9, 18, 15, 12]

# Moyenne
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne}")

# Valeur la plus fréquente
frequence_max = 0
valeur_plus_frequente = None

for note in notes:
    compteur = 0
    for n in notes:
        if n == note:
            compteur += 1
    
    if compteur > frequence_max:
        frequence_max = compteur
        valeur_plus_frequente = note

print(f"Valeur la plus fréquente : {valeur_plus_frequente}")