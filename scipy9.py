#sine wave for dft application
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
from scipy import fftpack
A = fftpack.fft(a)
frequency = fftpack.fftfreq(len(a)) * f_samp
figure, axis = plt.subplots()
axis.stem(frequency, np.abs(A))
axis.set_xlabel('Frequency in Hz')
axis.set_ylabel('Frequency Spectrum Magnitude')
axis.set_xlim(-f_samp / 2, f_samp/ 2)
axis.set_ylim(-5, 110)
plt.show()
