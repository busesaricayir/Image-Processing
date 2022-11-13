import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("img/img4.png")
image = cv2.resize(image, (500, 600))

# image = cv2.medianBlur(image, 3)
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=5)
final_img = clahe.apply(image_bw) + 30

_, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)

plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(ordinary_img, cmap='gray')
plt.title('Ordinary Threshold'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(final_img, cmap='gray')
plt.title('CLAHE image'), plt.xticks([]), plt.yticks([])

plt.show()
