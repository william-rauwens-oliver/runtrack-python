def my_long_word(longueur_min, phrase):
    mots = phrase.split()

    phrase_de_mots = []
    for mot in mots:
        nombres_caracteres = 0
        for caractere in mot:
            nombres_caracteres += 1
        if nombres_caracteres > longueur_min:
            phrase_de_mots.append(mot)
    return " ".join(phrase_de_mots)

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance") # j'ai repris la meme phrase que l'exemple, j'avais pas d'idée
print("Output :", resultat)