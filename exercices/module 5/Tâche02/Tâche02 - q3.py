solde = 250.00

try:
    montant = float(input("Montant à retirer : $"))

    if montant <= 0:
        raise ValueError("Erreur : le montant doit être supérieur à zéro.")

    if montant > solde:
        raise ValueError("Erreur : fonds insuffisants.")

except ValueError as erreur:
    if "could not convert" in str(erreur):
        print("Erreur : veuillez entrer un nombre valide.")
    else:
        print(erreur)

else:
    solde -= montant
    print("Retrait accepté.")
    print(f"Nouveau solde : {solde:.2f} $")

finally:
    print("Fin de la transaction.")