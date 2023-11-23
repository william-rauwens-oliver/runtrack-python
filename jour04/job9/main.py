L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maximum = L[0]
minimum = L[0]

for i in L[1:]:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("La valeur max est :", maximum)
print("La valeur min est :", minimum)