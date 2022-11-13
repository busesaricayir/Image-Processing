import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
roberts_cross_v = np.array([[1, 0],
                            [0, -1]])
roberts_cross_h = np.array([[0, 1],
                            [-1, 0]])
img = cv2.imread("img/img2.png", 0).astype('float64')
img /= 255.0
vertical = ndimage.convolve(img, roberts_cross_v)
horizontal = ndimage.convolve(img, roberts_cross_h)
edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
edged_img *= 255
plt.subplot(1, 2, 1), plt.imshow(img)
plt.title('Orginal')
plt.subplot(1, 2, 2) ,plt.imshow(edged_img)
plt.title('Robert_Cross')
plt.show()