while True:
    nom = input("Entrez votre nom : ")
    age_str = input("Entrez votre âge : ")

    try:
        age = int(age_str)  # conversion en entier
        print(f"{nom}, dans 5 ans, tu auras {age + 5} ans.")
        break
    except ValueError:
        print("Erreur : veuillez entrer un âge valide (nombre entier).")