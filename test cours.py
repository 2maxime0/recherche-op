import scipy
import numpy as np

A = np.array([[7, -2],
              [0, 1],
              [2, -2]])

b = np.array([14, 3, 3])

c = np.array([4, -2])

bounds = [(0, 2), (0, None)]

print(scipy.optimize.linprog(-c, A_ub=A, b_ub=b, bounds=bounds))

