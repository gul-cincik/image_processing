import cv2
import numpy as np

image =cv2.imread('sayfa.jpg')
ret, threshold = cv2.threshold(image,12,255, cv2.THRESH_BINARY)

griton = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, threshold_gri = cv2.threshold(griton,12,255, cv2.THRESH_BINARY)

gaussian = cv2.adaptiveThreshold(griton,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

ret,otsu = cv2.threshold(griton, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('orijinal', image)
cv2.imshow('threshold',threshold)
cv2.imshow('gaussian',gaussian)
cv2.imshow('otsu',otsu)
cv2.waitKey()
cv2.destroyAllWindows()