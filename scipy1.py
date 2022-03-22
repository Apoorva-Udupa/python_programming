#file input/output package:
import numpy as np
from scipy import io as sio #import io package
array = np.ones((4,4)) #create 4X4 array of ones
sio.savemat('F:\\example.mat',{'ar':array}) #store array in mat file
data = sio.loadmat('F:\\example.mat', struct_as_record = True) #load mat file and get data
print(data['ar'])

