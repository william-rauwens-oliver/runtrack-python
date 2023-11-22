def moyenne(note1, note2, note3):
    return round((note1 + note2 + note3) / 3)
def moyenne_evaluer(moyenne_etudiant):
    if 15 <= moyenne_etudiant <= 20:
        return "Très bon élève"
    elif 11 <= moyenne_etudiant <= 14:
        return "Bon élève"
    elif 8 <= moyenne_etudiant <= 10:
        return "Élève moyen"
    elif 0 <= moyenne_etudiant <= 7:
        return "Élève devant faire des efforts"
    else:
        return "La moyenne n'est pas dans la plage attendue (0-20)"

note1 = float(input("Entrez la 1ère note : "))
note2 = float(input("Entrez la 2ème note : "))
note3 = float(input("Entrez la 3ème note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

print("La moyenne de l'étudiant est :", moyenne_etudiant)

commentaire = moyenne_evaluer(moyenne_etudiant)
print(commentaire)