import random
import time

# Demander le nombre de questions
nb_questions = int(input("Combien de questions voulez-vous résoudre ? "))

# Initialisation des compteurs
correctes = 0
incorrectes = 0
temps_total = 0

# Liste des opérations
operations = ['+', '-', '*', '/']

for i in range(1, nb_questions + 1):
    # Générer deux nombres aléatoires
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    # Choisir une opération aléatoire
    op = random.choice(operations)

    # Calculer la bonne réponse
    if op == '+':
        bonne_reponse = a + b
    elif op == '-':
        bonne_reponse = a - b
    elif op == '*':
        bonne_reponse = a * b
    elif op == '/':
        # éviter division par zéro et garder 2 décimales
        b = random.randint(1, 9)
        bonne_reponse = round(a / b, 2)

    # Poser la question et mesurer le temps
    print(f"Question {i}: {a} {op} {b} = ?")
    debut = time.time()
    try:
        reponse = float(input("Votre réponse : "))
    except ValueError:
        reponse = None
    fin = time.time()

    duree = round(fin - debut, 2)
    temps_total += duree

    # Vérifier la réponse
    if reponse == bonne_reponse:
        print(f"Correct! (temps: {duree}s)")
        correctes += 1
    else:
        print(f"Incorrect. La bonne réponse était {bonne_reponse} (temps: {duree}s)")
        incorrectes += 1

# Résultats finaux
print("\n--- Résultats ---")
print(f"Nombre de réponses correctes : {correctes}")
print(f"Nombre de réponses incorrectes : {incorrectes}")
print(f"Temps total passé : {temps_total:.2f} secondes")
print(f"Temps moyen par question : {temps_total/nb_questions:.2f} secondes")