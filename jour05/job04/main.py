def tapis(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j == n:
                print(" ", end="")
            else:
                print("#", end="")
        print()

taille = int(input("Entrez la taille du tapis : "))
tapis(taille)