import scipy
import numpy as np

A = np.array([[1, 1]])

b = np.array([80])

c = np.array([15, 8])

bounds = [(30, 80), (10, 30)]

print(scipy.optimize.linprog(-c, A_ub=A, b_ub=b, bounds=bounds))