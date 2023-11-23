def doublons_delete(liste):
    no_doublons = []
    for element in liste:
        if element not in no_doublons:
            no_doublons.append(element)
    liste.clear()
    liste.extend(no_doublons)

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
doublons_delete(L)
print("Liste avec les doublons supprimés :", L)