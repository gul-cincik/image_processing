import cv2
kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

while True:
    ret, goruntu = kamera.read() #goruntu alınıp alınamadığını
    #ret = kamera.set(3, 320) #3. bilgi width
    #ret = kamera.set(4, 320) #4. bilgi height
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Gri Ton ', griton)
    if cv2.waitKey(25) & 0xFF == ord('q'): #qya basınca kapanıyor
        break

kamera.release()
cv2.destroyAllWindows()