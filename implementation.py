import numpy as np

def read_input_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    return lines

def rechercheExhaustive(k, V, s):
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
                x = rechercheExhaustive(k, V, s - V[i])
                if x + 1 < m:
                    m = x + 1
            return m

#rechercjeDynamique function
def rechercheDynamique(k, V, s):
    #initialisation of the table
    T = np.zeros((k, s + 1))
    for i in range(k):
        T[i, 0] = 0
    for j in range(s + 1):
        T[0, j] = j
    #filling the table
    for i in range(1, k):
        for j in range(1, s + 1):
            if j >= V[i]:
                T[i, j] = min(T[i - 1, j], T[i, j - V[i]] + 1)
            else:
                T[i, j] = T[i - 1, j]
    return T[k - 1, s]

def rechercheGloutonne(k, V, s):
    m = 0
    while s > 0:
        if s >= V[k - 1]:
            s = s - V[k - 1]
            m = m + 1
        else:
            k = k - 1
    return m

file = read_input_file('input.txt')

inputList = file[0].split()
S = inputList[0]
k = inputList[1]

dataList = file[1].split()
for i in range(len(dataList)):
    dataList[i] = int(dataList[i])

print("Recherche Exhaustive: ", rechercheExhaustive(int(k), dataList, int(S)))
print("Recherche Dynamique: ", rechercheDynamique(int(k), dataList, int(S)))
print("Recherche Gloutonne: ", rechercheGloutonne(int(k), dataList, int(S)))


