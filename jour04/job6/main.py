nombre = [1, 2, 3, 4, 5]

print("Avant l'échange :", nombre)
nombre[0], nombre[-1] = nombre[-1], nombre[0]
print("Après l'échange :", nombre)

# avec fontion

def echange(nombre):
    print("Avant l'échange :", nombre)
    nombre[0], nombre[-1] = nombre[-1], nombre[0]
    print("Après l'échange :", nombre)

L = [1, 2, 3, 4, 5]
echange(L)