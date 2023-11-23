def arrondir_nombre(nombre):
    partie_entiere = int(nombre)
    partie_decimale = nombre - partie_entiere
    return partie_entiere + 1 if partie_decimale >= 0.5 else partie_entiere
liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range(9):
    liste_nombres[i] = arrondir_nombre(liste_nombres[i])
n = 9
for i in range(n):
    for j in range(n - i - 1):
        if liste_nombres[j] > liste_nombres[j + 1]:
            liste_nombres[j], liste_nombres[j + 1] = liste_nombres[j + 1], liste_nombres[j]
print("Liste arrondie et triée :", liste_nombres)