montant_investissement = 10000
taux_rendement_annuel = 0.1

gain_annuel = taux_rendement_annuel * montant_investissement
print("Gain annuel initial pour la vente d'ensembles Nike : ", gain_annuel)

montant_investissement += gain_annuel
montant_investissement += 5000
taux_rendement_annuel = 0.12

nouveau_gain_annuel = taux_rendement_annuel * montant_investissement
print("Nouveau gain annuel après augmentation : ", nouveau_gain_annuel)
montant_investissement += nouveau_gain_annuel

montant_retire = 0.1 * montant_investissement
montant_investissement -= montant_retire
taux_rendement_annuel -= 0.01

new_gain_final = taux_rendement_annuel * montant_investissement
print('Gain Final', new_gain_final)
montant_final = (taux_rendement_annuel * montant_investissement) + montant_investissement
print("Montant final après retrait pour la vente d'ensembles Nike :", montant_final)