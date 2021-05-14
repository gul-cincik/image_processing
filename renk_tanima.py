import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while(1):
    ret,frame = kamera.read()

    #renk filtrelemesinde hsvye çevirmek daha kolay çalışmayı sağlar
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_kirmizi = np.array([150,30,30])
    upper_kirmizi = np.array([190,255,255])

    mask = cv2.inRange(hsv,dusuk_kirmizi,upper_kirmizi)#filtreleme iki ton aralığını aldık
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('orijinal', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('sonResim', son_resim)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()