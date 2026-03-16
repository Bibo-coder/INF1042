def demander_nombre():
    nombre = float(input("Entrez une valeur numérique : "))
    return nombre

def multiplier_par_cinq(nombre):
    resultat = nombre * 5
    print("Le résultat est :", resultat)

def main():
    nombre = demander_nombre()
    multiplier_par_cinq(nombre)

main()