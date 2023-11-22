for nombre in range(101):
    if nombre not in [26, 37, 88]:
        print(nombre)


# Autre façons


for nombre in range(101):
    if nombre != 26 and nombre != 37 and nombre != 88:
        print(nombre)