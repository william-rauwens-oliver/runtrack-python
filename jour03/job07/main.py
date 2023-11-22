def affiche_type_developpeur(langage):
    if langage == "JavaScript":
        print("tu es un développeur web")
    elif langage == "Python":
        print("tu es un développeur IA")
    elif langage == "Java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un developpeur mobile")
    else:
        print("un jour, je serai le meilleur développeur...")

    
affiche_type_developpeur("JavaScript")
affiche_type_developpeur("Python")
affiche_type_developpeur("Java")
affiche_type_developpeur("reactjs")
affiche_type_developpeur("C++") # c++ ajouté comme exemple uniquement pour tester lorsque le langage n'est égal à aucune des conditions précédentes, pour montrer comment "else" agit.