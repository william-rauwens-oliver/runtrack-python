L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

valeur = 0
for nombre in L:
    if nombre % 2 == 0:
        valeur += nombre
print("Le résultat de la somme de toutes les valeurs paires est :", valeur)