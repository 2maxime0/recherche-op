import numpy as np

V = [1, 2, 5, 10, 20, 50, 100, 200]

def rendreMonnaie(somme):
    rendu = {1:0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0}
    i = 8
    while somme%V[i] == 0:
        rendu.get()

def rechercheExhaustive(k, V, s):
    if s < 0:
        return np.inf
    else:
        if s == 0:
            return 0
        else:
            m = s
            for i in range(k):
                x = rechercheExhaustive(k, V, s - V[i])
                if x+1 < m:
                    m = x+1
            return m

#Function AlgoProgDynamique
def AlgoProgDynamique(k, V, s):
    #Initialisation
    M = np.zeros((k, s+1))
    #Calcul
    for i in range(k):
        for j in range(s+1):
            if j < V[i]:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = min(M[i-1][j], M[i][j-V[i]]+1)
    return M[k-1][s]































)
