try:
    age = input("Entrez votre âge : ")

    if not age.isdigit():
        raise ValueError("Erreur : l'âge doit être un nombre entier.")

    age = int(age)

    print(f"Vous avez {age} ans.")

except ValueError as erreur:
    print(erreur)