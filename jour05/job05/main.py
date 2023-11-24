def cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            est_majuscule = lettre.isupper()
            letre_mal_rangé = chr((ord(lettre) - ord('A' if est_majuscule else 'a') + decalage) % 26 + ord('A')) # j'ai fait en sorte que les majuscules marchent
            resultat += letre_mal_rangé.lower() if not est_majuscule else letre_mal_rangé
        else:
            resultat += lettre
    return resultat

normal_message = "Jules César"
decalage = 3
message_decale = cesar(normal_message, decalage)
print(f"Message original: {normal_message}")
print(f"Message décalé: {message_decale}")