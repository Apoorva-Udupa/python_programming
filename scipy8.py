#descrete fourier transform - scipy.fftpack
from matplotlib import pyplot as plt
import numpy as np

#freq in Hz
f = 5
#sample rate
f_samp = 50
t = np.linspace(0,2,2*f_samp,endpoint = False)
a = np.sin(f*2*np.pi*t)
figure,axis = plt.subplots()
axis.plot(t,a)
axis.set_xlabel('Time(s)')
axis.set_ylabel('signal amplitude')
plt.show()
#You can see this. Frequency is 5 Hz and its signal repeats in 1/5 seconds – it's call as a particular time period.
