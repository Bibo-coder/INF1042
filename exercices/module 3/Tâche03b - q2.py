def peut_entrer(age):
    return age >= 18

age = int(input("Entrez votre age : "))

if peut_entrer(age):
    print("Vous pouvez entrer dans le club.")
else:
    print("Accès refusé. Vous devez avoir au moins 18 ans.")