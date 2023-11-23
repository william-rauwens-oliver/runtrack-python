def echange(nombre):
    print("Avant l'échange :", nombre)
    nombre[0], nombre[-1] = nombre[-1], nombre[0]
    print("Après l'échange :", nombre)

ma_liste = [1, 2, 3, 4, 5]
echange(ma_liste)