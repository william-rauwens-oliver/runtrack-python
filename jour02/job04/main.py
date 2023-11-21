while True:
    try:
        N = int(input("Entrez un entier N supérieur à zéro : "))
        if N > 0:
            for l in range(1, N+1):
                for i in range(1, 11):
                    print(i ,'x' ,l,'=', i * l)
            else:
                print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")