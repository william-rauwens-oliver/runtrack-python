alphabet_normal = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

print(' '.join(alphabet_normal[::-1]))


# # Exo + sans utiliser reverse

def alphabet_a_lenvers():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(alphabet)-1, -1, -1):
        print(alphabet[i], end=' ')

alphabet_a_lenvers()

# # Exo ++ Randomiser puis ranger l'alphabet de z à a

import random

def melanger_et_afficher_a_lenvers():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    alphabet_inverse = sorted(alphabet, reverse=True)
    
    print("Alphabet mélangé:", " ".join(alphabet))
    print("Alphabet trié de z à a:", " ".join(alphabet_inverse))

melanger_et_afficher_a_lenvers()