#ndimage library forimage related operation in scipy
'''SciPy Image Processing provides Geometrics transformation (rotate, crop, flip), image filtering (sharp and de nosing), display image, image segmentation, classification and features extraction.
MISC Package in SciPy contains prebuilt images which can be used to perform image manipulation task
'''
from scipy import misc,ndimage
from matplotlib import pyplot as plt
import numpy as np
panda = misc.face()
plt.imshow(panda)
plt.show()
#flip down image
flip_down = np.flipud(misc.face())
plt.imshow(flip_down)
plt.show()

#rotate imade
panda_rotate = ndimage.rotate(panda,135)
plt.imshow(panda_rotate)
plt.show()
