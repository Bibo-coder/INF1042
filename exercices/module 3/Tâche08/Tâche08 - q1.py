# Demander une heure à l'utilisateur
heure = int(input("Entrez une heure (0 à 23) : "))

# Conversion en format 12h
if heure == 0:
    print("12am")
elif 1 <= heure < 12:
    print(f"{heure}am")
elif heure == 12:
    print("12pm")
elif 13 <= heure <= 23:
    print(f"{heure - 12}pm")
else:
    print("Heure invalide")