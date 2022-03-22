#numerical integration in scipy
#single integration
from scipy import integrate
f = lambda x: x**2
integration = integrate.quad(f,0,1)
print(integration)
