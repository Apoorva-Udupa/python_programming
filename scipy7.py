#eigenvalues and eigenvector using linear algebra eig()
from scipy import linalg
import numpy as np
arr = np.array([[5,4],[6,3]])
eg_val,eg_vec = linalg.eig(arr)
print(eg_val)
print(eg_vec)
