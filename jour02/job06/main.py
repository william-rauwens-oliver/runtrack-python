for nombre in range(2, 1001):
    nombre_premier = True
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            nombre_premier = False
            break
    if nombre_premier:
        print(nombre)