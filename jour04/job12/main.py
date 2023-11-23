def avec_insertion(liste):
    for i in liste:
        valeur_courante = i
        position = liste.index(i)
        while position > 0 and liste[position - 1] > valeur_courante:
            liste[position] = liste[position - 1]
            position = position - 1
        liste[position] = valeur_courante

ma_liste = [12, 4, 5, 6, 7, 3, 1, 15]
avec_insertion(ma_liste)
print("Liste triée :", ma_liste)


# avec les tribulles


def avec_tribulles(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste
    
print(avec_tribulles([14, 8, 9, 32, 11, 12, 18, 19]))