import random

def code_secret(borne_min, borne_max):
    #choix du code de maniere aléatoire
    code = random.randint(borne_min,borne_max)
    print("Entrez un nombre entre:" ,borne_min," et " ,borne_max)
    #comparaison avec l'entrée utilisateur
    while True:
        reponse = input("choix du nombre:")
        if reponse == code:
            print("Gagné!")
            False
        elif reponse < code:
            print ("trop petit! Reesayez")
        elif reponse > code:
            print ("Trop grand! reesayez")
    return 0

code_secret(10,50)

