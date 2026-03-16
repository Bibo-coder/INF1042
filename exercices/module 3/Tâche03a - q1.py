def demander_nom():
    nom = input("Quel est votre nom ? ")
    return nom

def dire_bonjours(nom):
    print(f"Bonjours {nom}!")

def main():
    nom = demander_nom()
    dire_bonjours(nom)

main()