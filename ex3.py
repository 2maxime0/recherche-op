import scipy
import numpy as np

A = np.array([[3, 4, 1, -3, -2],[5, 2, 2, -2, -3],[2, 3, 5, -3, -3]])

b = np.array([0, 0, 0])

c = np.array([120, 120, 120, -50, -60])

bounds = [(0, 100), (0, 100), (0, 200), (None, None), (None, None)]

print(scipy.optimize.linprog(-c, A_ub=A, b_ub=b, bounds=bounds))

#Test commit