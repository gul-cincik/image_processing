import cv2

kamera = cv2.VideoCapture('smile.mp4')#0 pcdeki kamera, usb ile kamera bağlamışsa 1,dosya alıyorsak direkt adı

while True:
    ret, goruntu = kamera.read() #goruntu alınıp alınamadığını
    cv2.imshow('Goruntu', goruntu)
    if cv2.waitKey(25) & 0xFF == ord('q'): #qya basınca kapanıyor
        break

kamera.release()
cv2.destroyAllWindows()