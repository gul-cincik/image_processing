import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('sudoku.JPG', 0)
resim = cv2.medianBlur(resim, 5)

ret, th1 = cv2.threshold(resim, 127, 255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(resim, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,2)#meande bir yeri eşikleme yaparken komşuluklarınınm ortalamasını alıyor 11 komşuya baktı
th3 = cv2.adaptiveThreshold(resim, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)#gaussianda ağırlıklı ortalamaya göre yapıyor.

basliklar = ['orijinal', 'basit thresholding', 'mean', 'gaussian']
resimler = [resim, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(resimler[i], 'gray')
    plt.title([basliklar[i]])
    plt.xticks([]), plt.yticks([])

plt.show()
