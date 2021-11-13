# Copyright Killian Steunou
#%% définition des variables :
import random
import time 
from copy import deepcopy
import os

clavier = 'azertyuiopqsdfghjklmwxcvbn'
lettres_clavier=[letter for letter in clavier]


#dictionnaire contenant les cartes
cards = {"Métier":[],"Action":[], "Culture générale":[], 
"Animal":[]
}

pwd = os.getcwd() #set the present working directory

#on récupère les mots à partir du fichier
file_name = "/Mots_Times_up.csv"
file_ref = open(pwd + file_name, 'r')
all_w = []

for line in file_ref.readlines():
    all_w.append(line)
jobs = all_w[0]
actions = all_w[1]
animals = all_w[2]
cultures = all_w[3]

#on transforme les string en tableau en coupant aux virgules
tab_jobs = jobs.split(',')
tab_actions = actions.split(',')
tab_animals = animals.split(',')
tab_cultures = cultures.split(',')

#on supprime les éventuels espaces au début et à la fin de chaque mot
for i in range(len(tab_jobs)):
    tab_jobs[i] = tab_jobs[i].strip()
for i in range(len(tab_actions)):
    tab_actions[i] = tab_actions[i].strip()
for i in range(len(tab_animals)):
    tab_animals[i] = tab_animals[i].strip()
for i in range(len(tab_cultures)):
    tab_cultures[i] = tab_cultures[i].strip()

#on supprime les titres de catégories
del tab_jobs[0]
del tab_actions[0]
del tab_animals[0]
del tab_cultures[0]

cards["Métier"] = tab_jobs
cards["Action"] = tab_actions
cards["Culture générale"] = tab_cultures
cards["Animal"] = tab_animals

lst_category = list(cards.keys())
#%% Le jeu

""" à 4 joueurs : joueur 1 doit jouer en équipe avec joueur 3, et joueur 2 avec joueur 4
    à 6 joueurs : joueur 1, 3 et 5 jouent ensemble, joueur 2, 4 et 6 ensemble"""

temps=60

def Partie(nb_joueurs):
    #on crée un dictionnaire plus petit qui ne contient que 40 valeurs (10 de chaque catégorie)
    true_dict = {"Métier":random.sample(cards["Métier"], 10),
                "Action":random.sample(cards["Action"],10),
                "Culture générale":random.sample(cards["Culture générale"],10),
                "Animal":random.sample(cards["Animal"],10)
    }
    #on crée autant de copies des listes qu'il y a de manches (3)

    little_dict1 = deepcopy(true_dict)
    little_dict2 = deepcopy(true_dict)
    little_dict3 = deepcopy(true_dict)

    lst_category1 = deepcopy(lst_category)
    lst_category2 = deepcopy(lst_category)
    lst_category3 = deepcopy(lst_category)

    while True:
        if input("Démarrer la partie ? (o/n) : ") in ('oui','o','yes','y'):
            print("Manche 1")
            print("")
            if input("Tapez une lettre pour démarrer, ENTRÉE pour quitter : ") in lettres_clavier:
                print("")
                Jeu(little_dict=little_dict1, nb_joueurs=nb_joueurs, lst_category=lst_category1)
                print("Manche 2")
                print("")
                if input("Tapez une lettre pour démarrer, ENTRÉE pour quitter : ") in lettres_clavier:
                    print("")
                    Jeu(little_dict=little_dict2, nb_joueurs=nb_joueurs, lst_category=lst_category2)
                    print("Manche 3")
                    print("")
                    if input("Tapez une lettre pour démarrer, ENTRÉE pour quitter : ") in lettres_clavier:
                        print("")
                        Jeu(little_dict=little_dict3, nb_joueurs=nb_joueurs, lst_category=lst_category3)
                    else:
                        print("")
                        print("À bientot !")
                        break
                else:
                    print("")
                    print("À bientot !")
                    break
            else:
                print("")
                print("À bientot !")
                break
        else:
            print("Cool.")
            break
        print("La partie est finie !")


def Jouer(start_timer, little_dict, lst_category):
    points = 0
    while True:
        #vérifier que la liste des catégories n'est pas vide avant d'y choisir la catégorie
        if lst_category:
            categ = random.choice(lst_category)
            if little_dict[categ]: #si la catégorie n'est pas vide
                word = random.choice(little_dict[categ])
            else:
                #on supprime l'indice vide
                lst_category.remove(categ)
                #on revérifie que la liste de catégorie n'est pas vide
                if lst_category:
                    categ = random.choice(lst_category)
                    if little_dict[categ]: #si la liste n'est pas vide
                        word = random.choice(little_dict[categ])
                    else:
                        print("C'était la dernière carte.")
                        break
                else:
                    print("C'était la dernière carte.")
                    break              
            bol = False
            while bol == False:
                bol = True
                if not(little_dict[categ]):
                    categ = random.choice(lst_category)
                    word = random.choice(little_dict[categ])
                    bol = False
            print("Vous devez faire deviner : {}\nCatégorie : {}\n                                                   Temps restant : {} secondes".format(word, categ, str(int(round(start_timer + temps - time.time(),0)))))
            if time.time() < start_timer + temps:
                suivant = input("\nAppuyez sur une lettre pour valider, ENTRÉE pour passer : ")
                print("")
                if suivant in lettres_clavier:
                    little_dict[categ].remove(word)
                    points += 1
            else:
                print("Times up ! Vous avez fait deviner {} mots. Bravo !\n".format(str(points)))
                break
    return points

def joueur_prêt():
     input("Prêt ?\nAppuyez sur ENTRÉE pour commencer : ")


def Jeu(little_dict, nb_joueurs, lst_category):
    points_J1 = 0
    points_J2 = 0
    points_J3 = 0
    points_J4 = 0
    points_J5 = 0
    points_J6 = 0
    points_totaux = 0
    
    
    while points_totaux < 40:
        if nb_joueurs in (1,2,3,4,5,6):
            for i in range(1,nb_joueurs + 1):
                if i == 1:
                    print("Joueur 1")
                    joueur_prêt()
                    start = time.time()
                    points = Jouer(start_timer=start, little_dict=little_dict, lst_category=lst_category)
                    points_J1 += points
                    points_totaux += points
                elif i == 2:
                    print("Joueur 2")
                    joueur_prêt()
                    start = time.time()
                    points = Jouer(start_timer=start, little_dict=little_dict, lst_category=lst_category)
                    points_J2 += points
                    points_totaux += points
                elif i == 3:
                    print("Joueur 3")
                    joueur_prêt()
                    start = time.time()
                    points = Jouer(start_timer=start, little_dict=little_dict, lst_category=lst_category)
                    points_J3 += points
                    points_totaux += points_J3
                elif i == 4:
                    print("Joueur 4")
                    joueur_prêt()
                    start = time.time()
                    points = Jouer(start_timer=start, little_dict=little_dict, lst_category=lst_category)
                    points_J4 += points
                    points_totaux += points_J4
                elif i == 5:
                    print("Joueur 5")
                    joueur_prêt()
                    start = time.time()
                    points = Jouer(start_timer=start, little_dict=little_dict, lst_category=lst_category)
                    points_J5 += points
                    points_totaux += points
                elif i == 6:
                    print("Joueur 6")
                    joueur_prêt()
                    start = time.time()
                    points = Jouer(start_timer=start, little_dict=little_dict, lst_category=lst_category)
                    points_J6 += points
                    points_totaux += points
        else:
            print("Veuillez saisir un nombre entre 1 et 6.")
            print("")
            nb_joueurs = int(input('Combien de joueurs ? (Maximum 6) : '))

    print("La manche est terminée !")
    print("Joueur 1 a {} points".format(points_J1))
    print("Joueur 2 a {} points".format(points_J2))
    print("Joueur 3 a {} points".format(points_J3))
    print("Joueur 4 a {} points".format(points_J4))
    print("Joueur 5 a {} points".format(points_J5))
    print("Joueur 6 a {} points".format(points_J6))
    print("")

try:
    print("\nBienvenue dans le Times Up!\nVous pouvez stopper la jeu à tout moment avec la commande ctrl + c.\n")
    nb_joueurs = int(input('Combien de joueurs ? (Maximum 6) : '))
    Partie(nb_joueurs)
except KeyboardInterrupt:
    print("\nVous avez arrêté le jeu. À bientot!")
#%%
