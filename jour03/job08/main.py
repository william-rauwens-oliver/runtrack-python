def affiche_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
         print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
         print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
         print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
         print("artichaut, aubergine, navet")
    else:
         print("Aucune correspondance trouvée")


affiche_aliments("fruits", "hiver")
affiche_aliments("fruits", "ete")
affiche_aliments("legume", "hiver")
affiche_aliments("legume", "ete")
affiche_aliments("poisson", "printemps") # exemple ajouté uniquement pour tester lorsque le type et la saison n'est égal à aucune des conditions précédentes, pour montrer comment "else" agit.