# Demander les informations à l'utilisateur
pointes = int(input("Nombre total de pointes : "))
eleves = int(input("Nombre d'élèves : "))

# Calculs
pointes_par_eleve = pointes // eleves
reste = pointes % eleves

# Affichage des résultats
print(f"Chaque élève reçoit : {pointes_par_eleve} pointe(s)")
print(f"Pointes restantes : {reste}")