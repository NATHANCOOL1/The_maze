import random
print("bienvenue dans le jeux du nombre")
print("se jeux est tres simple les du jeux ces que l'ordinateur va choisir un nombre aleatoire est votre but est de trouver le nombre que l'ordinateur a choisr qui est de 0 et 255 et l'ordinateur va vous dire si c'est plus grand ou plus petit ")
reponse = input("voulez vous jouer?/")
if reponse != "oui":
    quit()
nombre_a_deviner = random.randint(0,255)
nombre_tentative =100
while nombre_tentative >0:
    nombre_a_donner = int(input("donne moi un nombre/"))
    if nombre_a_deviner < nombre_a_donner:
        print("c'est moins")
        nombre_tentative = nombre_tentative-1
    elif nombre_a_deviner > nombre_a_donner:
        print("c'est plus")
        nombre_tentative = nombre_tentative-1
    else:
        break
    
if nombre_tentative != 0:
    print("GG il te restait",nombre_tentative)
    input("/quit")
else:
    print("tu as perdu")

