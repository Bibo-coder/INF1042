# Ibrahim Moumneh
import random

# Compteurs de score
gagnes = 0
pertes = 0

# Liste des choix possibles
choix_possibles = ["pierre", "papier", "ciseaux"]

continuer = True

while continuer:
    # Demander le choix de l'utilisateur
    joueur = input("Choisissez pierre, papier ou ciseau : ").lower()

    # Vérification du choix
    if joueur not in choix_possibles:
        print("Choix invalide, réessayez.")
        continue

    # Choix de l'ordinateur
    ordinateur = random.choice(choix_possibles)

    print("L'ordinateur a choisi :", ordinateur)

    # Déterminer le résultat
    if joueur == ordinateur:
        print("Égalité !")
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "papier" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "papier"):
        print("Vous avez gagnée !")
        gagnes += 1
    else:
        print("Vous avez perdu !")
        pertes += 1

    # Afficher le score
    print(f"Score → Gagnée : {gagnes} | Pertes : {pertes}")

    # Demander si l'utilisateur veut continuer
    reponce = input("Voulez-vous continuer ? (oui/non) : ").lower()
    if reponce != "oui":
        continuer = False

print("Merci d'avoir joué ! ")