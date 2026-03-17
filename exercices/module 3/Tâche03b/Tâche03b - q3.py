def sortie_permise(temperature, pluie):
    return temperature >= 15 and pluie == "non"

temperature = float(input("Entrez la température : "))
pluie = input("Est-ce qu'il pleut ? (oui/non) : ")

if sortie_permise(temperature, pluie):
    print("Sortie permise")
else:
    print("On reste dedans")