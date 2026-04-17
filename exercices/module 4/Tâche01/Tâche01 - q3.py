while True:
    a_str = input("Entrez la première valeur (a) : ")
    b_str = input("Entrez la deuxième valeur (b) : ")

    try:
        a = float(a_str)
        b = float(b_str)

        print(f"Produit : {a * b}")
        print(f"Différence (a - b) : {a - b}")
        break
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides (ex: 3.5, -2.1).")