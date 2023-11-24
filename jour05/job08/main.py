def my_sort(liste):
    coups, echanges_effectues = 0, True
    resultat_sortie = liste.copy()
    while echanges_effectues:
        echanges_effectues = False
        for i in range(len(resultat_sortie) - 1):
            if resultat_sortie[i] > resultat_sortie[i + 1]:
                resultat_sortie[i], resultat_sortie[i + 1] = resultat_sortie[i + 1], resultat_sortie[i]
                coups, echanges_effectues = coups + 1, True
    return resultat_sortie, coups

ma_liste = [64, 34, 25, 12, 22, 11, 90]
resultat, coups = my_sort(ma_liste)
print("Liste triée:", resultat)
print("Nombre total de coups nécessaires pour trier la liste :", coups)