import random

eleves = {"Maksym", "Léo", "Hayden", "Angel", "Ibrahim",
          "Josh", "Grant", "Maxime", "David"}

liste = list(eleves)

while liste:
    choix = random.choice(liste)
    print("Choisi :", choix)
    liste.remove(choix)