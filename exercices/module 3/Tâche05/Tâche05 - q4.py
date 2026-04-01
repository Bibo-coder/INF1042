def valider_mot_de_passe(mot_de_passe):
    # Vérifier les conditions
    a_un_chiffre = False
    a_une_lettre = False

    for caractere in mot_de_passe:
        if caractere.isdigit():
            a_un_chiffre = True
        if caractere.isalpha():
            a_une_lettre = True

    longueur_valide = len(mot_de_passe) >= 8

    # Retourner True si toutes les conditions sont respectées
    return a_un_chiffre and a_une_lettre and longueur_valide


# Exemple d'utilisation
mdp = input("Entrez un mot de passe : ")

if valider_mot_de_passe(mdp):
    print("Mot de passe valide")
else:
    print("Mot de passe invalide")