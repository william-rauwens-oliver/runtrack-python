L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

valeur_produit = 1

for valeur in L:
    if 25 <= valeur <= 90:
        valeur_produit *= valeur
        
print("Le produit de toutes les valeurs de la liste est :", valeur_produit)