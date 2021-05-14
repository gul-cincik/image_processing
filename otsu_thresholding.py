import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('gurultuluresim.JPG', 0)

ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(image,(5,5), 0)
ret,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

resimler = [image, 0, th1,
            image, 0, th2,
            blur, 0, th3]

basliklar = ['orijinal', 'Histogram','Basit Thresholding(127)',
             'orijinal', 'Histogram', 'otsuthresholding',
             'Gaussian Blur', 'Histogram', 'Otsu Thresholding']

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(resimler[i*3], 'gray')
    plt.title(basliklar[i*3]), plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2), plt.hist(resimler[i*3].ravel(),256)
    plt.title(basliklar[i*3+1]), plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(resimler[i*3+2], 'gray')
    plt.title(basliklar[i*3+2]),plt.xticks([]),plt.yticks([])

plt.show()