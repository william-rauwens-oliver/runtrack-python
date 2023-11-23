def tri_insertion(liste):
    for i in liste:
        valeur_courante = i
        position = liste.index(i)
        while position > 0 and liste[position - 1] > valeur_courante:
            liste[position] = liste[position - 1]
            position = position - 1
        liste[position] = valeur_courante

ma_liste = [12, 4, 5, 6, 7, 3, 1, 15]
tri_insertion(ma_liste)
print("Liste triée :", ma_liste)