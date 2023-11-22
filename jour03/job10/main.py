def pair_impair(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        return "Veuillez entrer un nombre entier positif."
    resultat = "pair" if nombre % 2 == 0 else "impair"
    return "{} est un nombre {}.".format(nombre, resultat)

resultat_1 = pair_impair(4)
resultat_2 = pair_impair(7)
resultat_3 = pair_impair(12.5)

print(resultat_1)
print(resultat_2)
print(resultat_3)