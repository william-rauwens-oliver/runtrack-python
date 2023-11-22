def type_developpeur(langage):
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

    
type_developpeur("JavaScript")
type_developpeur("Python")
type_developpeur("Java")
type_developpeur("reactjs")
type_developpeur("C++") # c++ ajouté comme exemple uniquement pour tester lorsque le langage n'est égal à aucune des conditions précédentes, pour montrer comment "else" agit.