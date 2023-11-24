def cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            majuscule = lettre.isupper()
            lettre = lettre.upper()
            decalee = chr((ord(lettre) - ord('A') + decalage) % 26 + ord('A'))
            if not majuscule:
                decalee = decalee.lower()
            resultat += decalee
        else:
            resultat += lettre
    return resultat

message_original = "Jules César"
decalage = 3
message_decale = cesar(message_original, decalage)
print(f"message original : {message_original}")
print(f"message décalé : {message_decale}")