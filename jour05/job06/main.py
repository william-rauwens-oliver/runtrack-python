def toilettes(hauteur_pour_marches, marches):
    distance_marches = hauteur_pour_marches * 2 / 100
    distance_jour = distance_marches * marches * 5
    distance_semaine = distance_jour * 7
    print("Pour", marches, "marches de", hauteur_pour_marches, "cm, le gardien parcourt", round(distance_semaine, 2), "m par semaine.")

toilettes(10, 20)