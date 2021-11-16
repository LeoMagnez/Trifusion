import random
import time

start_time = time.time()
def trifusion(tableau):
    if len(tableau) <= 1:
        return tableau
    pivot = len(tableau) //2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = trifusion(tableau1)
    droite = trifusion(tableau2)
    fusionne = fusion(gauche, droite)
    print(gauche)
    print(droite)
    return fusionne

def fusion(tableau1, tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1]<tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1+=1
        else:
             tableau_fusionne.append(tableau2[indice_tableau2])
             indice_tableau2+=1

    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1

    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    print(tableau_fusionne)
    return tableau_fusionne


def randlist():
    tableau = []
    taille_max = 1000000
    rang_max = 0
    while rang_max<taille_max:
        randnumber = random.randint(0, 10000000)
        tableau.append(randnumber)
        rang_max+=1
    return tableau


end_time = time.time()
tableau = randlist()
print(tableau)
tableau_tri = trifusion(tableau)
print(tableau_tri)
print("Tri effectué en "+ str(end_time-start_time))
input("g fini bg")
