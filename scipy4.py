#scipy linear algebra library
#input: 2d array Output:2d array
#determinant
from scipy import linalg
import numpy as np
two_d_ar = np.array([[4,5],[3,2]])
print(linalg.det(two_d_ar))
