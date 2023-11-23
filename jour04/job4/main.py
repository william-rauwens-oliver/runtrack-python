def fruits():
    fruits_appel = ["pomme", "cerise", "orange", "melon"]
    fruits_appel.insert(2, "Mangue")
    return fruits_appel

resultat = fruits()
print(resultat)

# écraser orange pour remplacer par mangue.

def fruits():
    fruits_appel = ["pomme", "cerise", "orange", "melon"]
    fruits_appel[2] = "mangue"
    return fruits_appel

resultat = fruits()
print(resultat)