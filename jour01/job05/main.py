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
    
    def trier_de_z_a_a(une_liste):
        for i in range(len(une_liste) - 1):
            for j in range(i + 1, len(une_liste)):
                if ord(une_liste[i]) < ord(une_liste[j]):
                    une_liste[i], une_liste[j] = une_liste[j], une_liste[i]
        return une_liste
    
    alphabet_trie_inverse = trier_de_z_a_a(alphabet)
    
    print("Alphabet mélangé:", " ".join(alphabet))
    print("Alphabet trié de z à a:", " ".join(alphabet_trie_inverse))

melanger_et_afficher_a_lenvers()