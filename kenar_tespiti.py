import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while(1):
    ret,frame = kamera.read()

    #renk filtrelemesinde hsvye çevirmek daha kolay çalışmayı sağlar
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_kirmizi = np.array([150,30,30])
    upper_kirmizi = np.array([190,255,255])

    """laplacian = cv2.Laplacian(frame, cv2.CV_64F)#tipi
    sobelX = cv2.Sobel(frame, cv2.CV_64F, 1, 0,ksize=5)
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 0, 1,ksize=5)"""

    kenarlar = cv2.Canny(frame, 100, 200)
    kenarlar2 = cv2.Canny(frame, 150, 300)

    mask = cv2.inRange(hsv,dusuk_kirmizi,upper_kirmizi)#filtreleme iki ton aralığını aldık
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('orijinal', frame)
    #cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelX', sobelX)
    #cv2.imshow('sobelY', sobelX)
    cv2.imshow('kenarlar',kenarlar)
    cv2.imshow('kenarlar2', kenarlar2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()