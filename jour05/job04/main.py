def tapis(taille):
    for i in range(taille + 1):
        for j in range(taille + 1):
            if i + j == taille:
                print(" ", end="")
            else:
                print("#", end="")
        print()

taille = int(input("Entrez la taille du tapis : "))
tapis(taille)