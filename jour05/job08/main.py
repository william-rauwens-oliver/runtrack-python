def my_sort(liste):
    n = len(liste)
    echanges = 0
    resultat_sortie = liste.copy()
    echanges_effectues = True
    while echanges_effectues:
        echanges_effectues = False
        for i in range(n-1):
            if resultat_sortie[i] > resultat_sortie[i+1]:
                resultat_sortie[i], resultat_sortie[i+1] = resultat_sortie[i+1], resultat_sortie[i]
                echanges += 1
                echanges_effectues = True
    return resultat_sortie, echanges

ma_liste = [64, 34, 25, 12, 22, 11, 90]
resultat, coups = my_sort(ma_liste)
print("Liste triée:", resultat)
print("Nombre total de coups nécessaires:", coups)