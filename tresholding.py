import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('gradient.JPG')#resim gri ton old çevirmedik

ret, thres1 = cv2.threshold(resim,127,255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(resim,127,255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(resim,127,255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(resim,127,255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(resim,127,255, cv2.THRESH_TOZERO_INV)

basliklar = ['orijinal_resim', 'binary', 'binary_inv', 'trunc', 'toZero', 'toZero_inv']

resimler = [resim, thres1, thres2, thres3, thres4, thres5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(resimler[i], 'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()

