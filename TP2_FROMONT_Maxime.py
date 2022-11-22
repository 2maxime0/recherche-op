#Imports
import scipy
import numpy as np

#Question 1(a)
def isThereNonInteger(x):
    for i in x:
        if i != int(i):
            return True
    return False

#Test question 1(a)
print(isThereNonInteger(np.array([1,2,3,4,5])))
print(isThereNonInteger(np.array([1,2,3,4,5.5])))

#Question 1(a) - 2
def firstNonInteger(x):
    for i in range(len(x)):
        if x[i] != int(x[i]):
            return i
    return -1

#Test question 1(a) - 2
print(firstNonInteger(np.array([1,2,3,4,5])))
print(firstNonInteger(np.array([1,2,3,4.5])))

#Question 1(c)
def branch(x, bounds):
    i = firstNonInteger(x)
    bound1 = bounds.copy()
    bound2 = bounds.copy()
    bound1[i] = (bounds[i][0], int(x[i]))
    bound2[i] = (int(x[i]) + 1, bounds[i][1])
    return bound1, bound2

#Test question 1(c)
print(branch(np.array([1,2,3,4,5]), [(0, 10)] * 5))

#Question 1(b) (Enoncé)
A = np.array([[2, 1, 3],
              [1, 0, 1],
              [0, 1, 1]])
b = np.array([10, 5, 5])
c = np.array([-1, -1, -3])
bounds = [(0, 10)] * 3
S = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=bounds)
print(S.x)
#Question 1(b) (Réponse)
bounds1, bounds2 = branch(S.x, bounds)
print("Bounds 3 : ", bounds1)
print("Bounds 2 : ", bounds2)

#Question 2(a)
# En parcourant un arbre de décision en largeur (Breath First Search), 
# on s'occupe d'abord de chaque noeuds sur le même niveau avant de descendre plus bas
#En parcourant un arbre de décision en profondeur (Depth First Search), 
# on descened tout en bas (le bas étant un noeud n'ayant aucun voisin) 
# avant de remonter et de passer au noeud suivant le plus proche récursivement 
# (avant de finalement remonter tout en haut pour passer au noeud suivant du haut et recommander)

#Question 2(b) - 1
#Parametres : S, bounds, x (par défaut None) et fun (par défaut np.inf)
#Retourne : Un tuple contenant la solution entière optimal et le minimum atteint pour cette solution ou un tuple contenant x et fun par défaut
#On vérifie si x = None
#   On prend la solution S.x
#Si X ne possède pas de valeur non entière
#   Si la valeur de la fonction objectif de S est inférieure à fun reçu
#       On met à jour fun avec la valeur de la fonction objectif de S
#       On met à jour x avec la solution de S
# On utilise la fonction branch pour diviser les bornes en deux
# On définit S1 comme la solution de linprog avec les bornes de bounds1
# On définit S2 comme la solution de linprog avec les bornes de bounds2
# On définit x1 et fun1 comme le résultat de branchAndBound avec S1, bounds1, x et fun
# On définit x2 et fun2 comme le résultat de branchAndBound avec S2, bounds2, x et fun
# Si fun1 est inférieur à fun2
#   On retourne x1 et fun1
# Sinon
#   On retourne x2 et fun2
# Sinon global
#   On retourne x et fun

#Je pensais que cet algorithme aurait pu marcher mais je me suis trompé car je n'arrive pas à faire fonctionner la fonction :(

#Question 2(b) - 2
def branchAndBound(S, bounds, x=None, fun=np.inf):
    if x is None:
        x = S.x
    if not isThereNonInteger(x):
        if S.fun < fun:
            fun = S.fun
            x = S.x
        bounds1, bounds2 = branch(x, bounds)
        S1 = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=bounds1)
        S2 = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=bounds2)
        x1, fun1 = branchAndBound(S1, bounds1, x, fun)
        x2, fun2 = branchAndBound(S2, bounds2, x, fun)
        if fun1 < fun2:
            return x1, fun1
        else:
            return x2, fun2
    else:
        return x, S.fun
#Cette fonction ne répond pas correctement à l'énoncé puisqu'elle ne renvoie que x et S.fun dans tout les cas. 
# J'essayais déjà d'avoir des bons résultats avant de l'améliorer.

#Test question 2(b) - 3
A = np.array([[2, 1, 3],
              [1, 0, 1],
              [0, 1, 1]])
b = np.array([10, 5, 5])
c = np.array([-1, -1, -3])
bounds = [(0, 10)] * 3
S = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=bounds)
print(branchAndBound(S, bounds))
print(branchAndBound(S, bounds, S.x, S.fun))

#Les résultats ne sont pas bons, je n'ai pas réussie à faire mieux, je suis désolé.

#Essai plus vieux non concluant :
def BnB2(S, bounds, x, fun):
    if S.success:
        if isThereNonInteger(S.x):
            print("La fonction renvoie la solution optimale")
            return S.x, np.dot(c, S.x)
        else:
            bounds1, bounds2 = branch(S.x, bounds)
            S1 = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=bounds1)
            S2 = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=bounds2)
            if S1.success:
                if isThereNonInteger(S1.x):
                    if np.dot(c, S1.x) < fun:
                        x = S1.x
                        fun = np.dot(c, S1.x)
                else:
                    x, fun = BnB2(S1, x, fun)
            if S2.success:
                if isThereNonInteger(S2.x):
                    if np.dot(c, S2.x) < fun:
                        x = S2.x
                        fun = np.dot(c, S2.x)
                else:
                    x, fun = BnB2(S2, x, fun)
            return x, fun
    else:
        print("La fonction renvoie x et fun")
        return x, fun

#Test question 2(b)
#print(BnB2(S, bounds, None, np.inf))