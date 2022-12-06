import numpy as np
import time
import matplotlib.pyplot as plt

#Question 11
def get_file_datas(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    inputList = lines[0].split()
    S = int(inputList[0])
    k = int(inputList[1])
    
    V = lines[1].split()
    if k != len(V):
        raise Exception("Erreur: k != longueur de V")
    for i in range(k):
        V[i] = int(V[i])

    return S, k, V

#Question 12 - 1
def rechercheExhaustive(k, V, s):
    start = time.time()
    i = 0
    m = 0
    x = 0
    if s < 0:
        return np.inf
    else:
        if s == 0:
            return 0
        else:
            m = s
            for i in range(k):
                if start + 60 >= time.time():
                    x = rechercheExhaustive(k, V, s - V[i])
                    if x + 1 < m:
                        m = x + 1
                else:
                    raise Exception("Erreur: rechercheExhaustive trop longue")
            return m

#Question 12 - 2
def rechercheDynamique(k, V, s):
    T = np.zeros((k, s + 1))
    for i in range(k):
        T[i, 0] = 0
    for j in range(s + 1):
        T[0, j] = j
    for i in range(1, k):
        for j in range(1, s + 1):
            if j >= V[i]:
                T[i, j] = min(T[i - 1, j], T[i, j - V[i]] + 1)
            else:
                T[i, j] = T[i - 1, j]
    return T[k - 1, s]

#Question 12 - 3
def rechercheGloutonne(k, V, s):
    m = 0
    while s > 0:
        if s >= V[k - 1]:
            s = s - V[k - 1]
            m = m + 1
        else:
            k = k - 1
    return m

#Affichage des résultats et partie de #Question 14
def print_every_recherche(k, V, s):
    start = time.time()
    print("Recherche exhaustive: ", rechercheExhaustive(k, V, s))
    end = time.time()
    print("Time: ", end - start)
    print("")

    start = time.time()
    print("Recherche dynamique: ", rechercheDynamique(k, V, s))
    end = time.time()
    print("Time: ", end - start)
    print("")

    start = time.time()
    print("Recherche gloutonne: ", rechercheGloutonne(k, V, s))
    end = time.time()
    print("Time: ", end - start)
    print("---------------------")

'''
#Test question 11 et Question 13
s1, k1, V1 = get_file_datas("01.test")
s2, k2, V2 = get_file_datas("02.test")
s3, k3, V3 = get_file_datas("03.test")
'''

'''
#Test question 12 et Question 13
print_every_recherche(k1, V1, s1)
print_every_recherche(k2, V2, s2)
print_every_recherche(k3, V3, s3)
'''

#Question 13
#Utilisation de plusieurs fichiers de test 01.test, 02.test, 03.test

#Question 14
#Affichage des temps automatique, et arrêt de la fonction rechercheExhaustive si elle prend plus de 60 secondes (compris dans fonction directement)
#Ce dessous, la fonction benchmark execute les tests n fois, et on retourne la moyenne des temps

def benchmark(n, k, V, s):
    #Initialisation des tableaux de temps d'execution
    temps_execution_exhaustive = []
    temps_execution_dynamique = []
    temps_execution_gloutonne = []

    for i in range(n):
        start = time.time()
        rechercheExhaustive(k, V, s)
        end = time.time()
        temps_execution_exhaustive.append(end - start)

        start = time.time()
        rechercheDynamique(k, V, s)
        end = time.time()
        temps_execution_dynamique.append(end - start)

        start = time.time()
        rechercheGloutonne(k, V, s)
        end = time.time()
        temps_execution_gloutonne.append(end - start)
    
    return np.mean(temps_execution_exhaustive), np.mean(temps_execution_dynamique), np.mean(temps_execution_gloutonne)

#'''

#Initialisation de s, k et V, ainsi que d si on utilise la monnaie expo
s = 17
d = 2
k = 4
V = [d**i for i in range (0, k)]
#s, k, V = get_file_datas("04.test")

#Initialisation du nombre d'itérations
n = 100

moyenne_temps_execution_exhaustive, moyenne_temps_execution_dynamique, moyenne_temps_execution_gloutonne = benchmark(n, k, V, s)
print("Temps d'exécution moyen de la recherche exhaustive: ", moyenne_temps_execution_exhaustive)
print("Temps d'exécution moyen de la recherche dynamique: ", moyenne_temps_execution_dynamique)
print("Temps d'exécution moyen de la recherche gloutonne: ", moyenne_temps_execution_gloutonne)

#'''

#Analyse des résultats
#On remarque que la recherche dynamique est la plus rapide, et la recherche exhaustive la plus lente.
#La recherche gloutonne est plus rapide que la recherche exhaustive, mais moins rapide que la recherche dynamique.
#La recherche gloutonne est donc la plus efficace, et la recherche exhaustive la moins efficace.
#La rcherche gloutonne est tellement efficace dans notre cas que sa moyenne est souvent arrondie par Python à 0.0
#On pourrait augmenter s ou augmenter le nombre d'itérations mais nous sommes limité par le long temps d'execution de la recherche exhaustive

'''
#Tentative d'affichages de courbe (ne fonctionne pas car je n'ai pas réussie à imorter matplotlib dans mon environnement)
s_max = 6
k_max = 4
d = 2
V = [d**i for i in range (0, k_max)]
n = 100

for s in range(1, s_max + 1):
    moyenne_temps_execution_exhaustive, moyenne_temps_execution_dynamique, moyenne_temps_execution_gloutonne = benchmark(n, k_max, V, s)
    fig, ax = plt.subplots(s_max, s_max)
    ax[0, 0].plot(s, moyenne_temps_execution_exhaustive)
    ax[0, 0].set_title("Temps d'execution moyen exhaustive pour S maximum = " + str(s_max))
    plt.show()
'''