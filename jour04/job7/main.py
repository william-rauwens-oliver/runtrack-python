L = [8, 24,48,2,16]

multiples_de_3 = 0

for nombre in L:
    if nombre % 3 == 0:
        multiples_de_3 +=1
print("Nombre contenant dans le multiples de 3 est :", multiples_de_3)