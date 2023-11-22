def moyenne(note1, note2, note3):
    return round((note1 + note2 + note3) / 3)

note1 = float(input("Entrez la 1ère note :"))
note2 = float(input("Entrez la 2ème note :"))
note3 = float(input("Entrez la 3ème note :"))

moyenne_etudiant = moyenne(note1, note2, note3)

print("La moyenne de l'étudiant est :", moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon éleve")
elif 11 <= moyenne_etudiant<= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("La moyenne n'est pas dans la plage attendue (0-20)") # cette ligne permet l'ajout de "else" si la moyenne est pas attendu, meme si cela est pas trop prossible car c'est obligatoirement entre 0 et 20