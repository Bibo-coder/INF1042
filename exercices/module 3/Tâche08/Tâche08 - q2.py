# Demander un nombre entier à l'utilisateur
n = int(input("Entrez un nombre entier : "))

# Vérifier la divisibilité
if n % 3 == 0 and n % 5 == 0:
    print("Le nombre est divisible par 3 et par 5.")
elif n % 3 == 0:
    print("Le nombre est divisible par 3.")
elif n % 5 == 0:
    print("Le nombre est divisible par 5.")
else:
    print("Le nombre n'est divisible ni par 3 ni par 5.")