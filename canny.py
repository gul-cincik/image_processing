import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('messi.jpg',0)#gri tonlamayla aldık
kenarlar = cv2.Canny(resim, 100,200)

plt.subplot(121), plt.imshow(resim, cmap='gray')#121 1 satır 2 sütun olacak ve 1. resmi koyacak
plt.title('orijinal'),plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(kenarlar, cmap='gray')
plt.title('kenarlar'),plt.xticks([]), plt.yticks([])
plt.show()

