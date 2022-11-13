import matplotlib.pyplot as plt
import cv2

img = cv2.imread('img/img3.png')

# 8 bit
imgs = [255 * ((img & (1 << i)) >> i) for i in range(8)]

for i in range(8):
    j = i + 1
    plt.subplot(2, 4, j), plt.imshow(imgs[i], cmap='gray')
plt.show()