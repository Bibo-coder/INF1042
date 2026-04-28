import pandas as pd

# 1) Charger le CSV
df = pd.read_csv("exercices/module 4/Tâche08/fictitious_basketball_league_players_1200_v2.csv")

# 2) Vérifier rapidement
print(df.head(5))      # aperçu
df.info()              # colonnes + types + non-nuls

# 3) Sélectionner des colonnes
print(df[["Player", "Team", "position", "ppg"]].head(10))

# 4) Filtrer des lignes (conditions)
elite = df[df["ppg"] >= 25]
print(elite[["Player", "Team", "ppg"]].head(10))

# 5) Trier + Top N
top_salary = df.sort_values("salary", ascending=False).head(10)
print(top_salary[["Player", "Team", "salary"]])

# 6) Compter par catégorie
print(df["position"].value_counts())      # nb de joueurs par position
print(df["Team"].value_counts().head(10)) # top 10 équipes par nb de joueurs

# 7) Statistiques rapides
print(df["ppg"].describe())

# 8) Regrouper (moyennes par position)
by_pos = df.groupby("position")[["ppg", "rebounds pg", "assists"]].mean().round(1)
print(by_pos)

# 9) Créer une nouvelle colonne (ex: efficacité simple)
df["impact"] = df["ppg"] + df["rebounds pg"] + df["assists"]

# 10) Convertir une colonne en nombre (si jamais elle est lue comme texte)
df["ppg"] = pd.to_numeric(df["ppg"], errors="coerce")

# 11) Gérer valeurs manquantes
print(df.isna().sum())
df = df.dropna(subset=["ppg"])            # enlever lignes où ppg est NaN (option)
# df["ppg"] = df["ppg"].fillna(0)         # ou remplacer (option)

# 12) Exporter un résultat en CSV
elite.to_csv("top_scorers.csv", index=False)
top_salary.to_csv("top_salary.csv", index=False)