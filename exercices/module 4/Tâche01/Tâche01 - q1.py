while True:
    nom = input("Entrez votre nom : ")

    if len(nom) < 8:
        print("Le nom doit contenir au moins 8 caractères.")
    elif len(nom) > 12:
        print("Le nom doit contenir au maximum 12 caractères.")
    else:
        print(f"Bonjour, {nom} !")
        break