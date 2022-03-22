from scipy import integrate
import numpy as np
from math import sqrt
f = lambda x,y: 64*x*y
#lowrlimit of second integral
p = lambda x: 0
#upperlimit of first integral
q = lambda y: sqrt(1-2*y**2)
integration = integrate.dblquad(f,0,2/4,p,q)
print(integration)
