nom_produit = "Album QALF Infinity"
prix_unitaire = 30
quantite_stock = 10

print("Produit: {}, Prix unitaire: {} €, Quantité en stock: {}".format(nom_produit, prix_unitaire, quantite_stock))

quantite_achetee = int(input("Combien d'unités souhaitez-vous acheter ? "))
quantite_stock -= quantite_achetee

prix_unitaire *= 1.1

for _ in range(quantite_achetee):
    prix_unitaire_arrondi = round(prix_unitaire, 2)
    formatted_prix_unitaire = "{:.2f} €".format(prix_unitaire_arrondi)
    print("Prix unitaire pour un album: {}".format(formatted_prix_unitaire))

prix_total = prix_unitaire * quantite_achetee
print("Prix total pour {} albums: {:.2f} €".format(quantite_achetee, prix_total))
print("Nouvelle quantité en stock: {}".format(quantite_stock))