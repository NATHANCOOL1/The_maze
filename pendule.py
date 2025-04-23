import random
choix = ["bascule","japonais","humour","trous","capitaine","assombrir","point","empaillage","bottes","larve"]
solution = random.choice(choix)
tentative = 7
affichage = ""
lettres_trouvees = ""
for i in solution:
    affichage = affichage + "_ "
print("bienvenue dans le jeu du pendu le but du jeux est que l'ordinateur va choisir un mot et le but c'est que toi, tu devines le mot que l'ordinateur a choisis. si vous avez une mauvaise reponse le pendu s'affichera petit a petit")
reponse = input("voulez vous jouer?/")
if reponse != "oui":
    quit()

while tentative > 0:
    print("Mot à deviner : ", affichage)
    proposition = input (" proposez une lettre : ")[0:1].lower()
    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("tu as trouver une lettre")

    else:
        tentative = tentative - 1
        
        if tentative == 0:
            print(" ==========Y= ")
        if tentative <= 1:
            print(" ||/       | ")
        if tentative <= 2:
            print(" ||        O ")
        if tentative <= 3:
            print(" ||       /|\ ")
        if tentative <= 4:
            print(" ||        | ")
        if tentative <= 5:
            print("/||       / \ ")
        if tentative <= 6:
            print("===============\n")
            
    
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "
    if "_ " not in affichage:
        print("tu as gagné")
        input("/quit")
        break