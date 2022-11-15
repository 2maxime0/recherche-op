import scipy
import numpy as np

A = np.array([[3, 4],
              [1, 3],
              [2, 2]])

b = np.array([4200, 2250, 2600])

c = np.array([66, 84])

#Correction
bounds = [(0, 1100), (0, None)]

print(scipy.optimize.linprog(-c, A_ub=A, b_ub=b, bounds=bounds))