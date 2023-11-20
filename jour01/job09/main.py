nom_produit = "Album QALF Infinity"
prix_unitaire = 100
quantite_stock = 10

print(f"Produit: {nom_produit}, Prix unitaire: {prix_unitaire} €, Quantité en stock: {quantite_stock}")

quantite_achetee = int(input("Combien d'unités souhaitez-vous acheter ? "))
quantite_stock += quantite_achetee

prix_unitaire *= 1.1

print(f"Produit: {nom_produit}, Nouveau prix unitaire: {prix_unitaire} €, Nouvelle quantité en stock: {quantite_stock}")