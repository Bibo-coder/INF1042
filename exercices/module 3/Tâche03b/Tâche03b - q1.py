def calcul_divisions(n):
    division = n / 4
    division_entiere = n // 4

    print("n / 4 =", division)
    print("n // 4 =", division_entiere)

n = int(input("Entrez un entier n :"))
calcul_divisions(n)