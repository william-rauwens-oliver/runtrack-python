montant_investissement = 10000
taux_rendement_annuel = 5 

gain_annuel = (taux_rendement_annuel / 100) * montant_investissement
print(f"Gain annuel initial pour la vente d'ensembles Nike : {gain_annuel} euros")

montant_investissement += 5000
taux_rendement_annuel += 2

nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_investissement
print(f"Nouveau gain annuel après augmentation : {nouveau_gain_annuel} euros")

montant_retire = 0.1 * montant_investissement
montant_investissement -= montant_retire
taux_rendement_annuel -= 1

montant_final = montant_investissement + nouveau_gain_annuel
print(f"Montant final après retrait pour la vente d'ensembles Nike : {montant_final} euros")