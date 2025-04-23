score =0
print("bienvenue au quiz")
reponse = input("veut tu jouer?:")
if reponse != "oui":
    quit()
    score =-999


reponse2 = input("quel est la couleur du ciel:")
if reponse2 == ("bleu"):
    print("bonne réponse")
    score +=1
elif ("bypass"):
    print("corret answer" \
    "answer 1 :oui/" \
    "answer 2 :bleu/" \
    "answer 3 :ou est la question 1/" \
    "answer 4 /:" \
    "answer 5 :ni quiz.py/")
else :
    print("faux")
    score+=-10

reponse3 =input("passons a la question 3:")
if reponse3 ==("ou est la question 1"):
   print("la question 1 était ('Veut tu jouer') ")
   score+=100

else :
    print("tu ne vois pas qu'il y a un problème")
    score+=-20

reponse4 =input("bon repassont a la question 3:")
if reponse4 ==(""):
    print("bonne réponse")
    score+=999
else :
    print("relie bien la question!!!")
    score+=-1

reponse5 =input("comment crée un fichier python:")
if reponse5 ==("ni quiz.py"):
    print("bonne réponse")
    score+=0.5
else :
    print("non la bonne réponse c'est ('ni quiz.py')")
    score+=-35
