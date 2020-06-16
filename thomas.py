import random

pendu = open("C:\\Users\\tomal\\OneDrive\Bureau\\partiel thomas\\Partiel_B1Game_S2_Python\\pendu.txt", "r")
liste = open("C:\\Users\\tomal\\OneDrive\Bureau\\partiel thomas\\Partiel_B1Game_S2_Python\\dict.txt", "r")

new_pendu = pendu.read()
new_liste = liste.read()
new_pendu = new_pendu.split(';')
new_liste = new_liste.split()


win = False
compteur = 0
i = 0
mot = random.choice(new_liste)

mot_en_lettre = list(mot)
vide = []

print("mot choisi , il a {} lettres a toi de les trouver !\n".format(len(mot)))

for i in range(len(mot_en_lettre)):
        print("_")  # a voir plus tard le saut de ligne...
while win != True and compteur <= 8:
    if compteur >=8:
        print("c est perdu ! (c etait ",mot,")...")
        break
    if mot_en_lettre == vide:
        print("gg wp , t as gagné")
        win = True   #meme si  c est aps utile car break ... :v
        break
    lettre = input("rentre une seule lettre seulement :   ")
    lettre = lettre.upper()
    if chr(48)<= lettre <= chr(57) :   #ne prend pas les cas de multiple lettres...
        print("non , tu dois mettre une seule LETTRE ! ")
    else:
        if (mot.find(lettre) != -1):
            print ("le mot contien bien la lettre ",lettre)
            mot_en_lettre.remove(lettre)
        else:
            print ("ta lettre n est pas dans le mot...")
            print(new_pendu[compteur])
            compteur +=1