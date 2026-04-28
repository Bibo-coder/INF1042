notes = [78, 85, 92, 67, 85, 74]

# 1. Affiche la liste complète
print("Liste complète :", notes)

# 2. Première et dernière note
print("Première note :", notes[0])
print("Dernière note :", notes[-1])

# 3. Ajouter 88
notes.append(88)

# 4. Supprimer première occurrence de 85
notes.remove(85)

# 5. Liste mise à jour
print("Liste mise à jour :", notes)

# 6. Calculs
total = sum(notes)
moyenne = total / len(notes)
max_note = max(notes)
min_note = min(notes)

print("Total :", total)
print("Moyenne :", moyenne)
print("Max :", max_note)
print("Min :", min_note)