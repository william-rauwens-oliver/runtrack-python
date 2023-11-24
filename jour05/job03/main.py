def triangle(hauteur):
    for i in range(hauteur):
        espaces = " " * (hauteur - i - 1)
        if i == hauteur - 1:
            ligne = "/" + "_" * (2 * i) + "\\"
        else:
            ligne = "/" + " " * (2 * i) + "\\"
        print(espaces + ligne)

hauteur = int(input("Entrez la hauteur du triangle : "))
triangle(hauteur)