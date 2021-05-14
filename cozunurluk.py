import cv2

kamera = cv2.VideoCapture(0)

def cozunurluk_1080p():
    kamera.set(3, 1920)#3. parametre width ve bunu 1920 yaptık
    kamera.set(4, 1080)#1920 genişliğinde 1080 yüksekliğinde

def cozunurluk_720p():
    kamera.set(3, 1280)#3. parametre width ve bunu 1280 yaptık
    kamera.set(4, 720)#1280 genişliğinde 720 yüksekliğinde

def cozunurluk_480p():
    kamera.set(3, 640)
    kamera.set(4, 480)

def cozunurluk_belirle(width, heigth):
    kamera.set(3, width)
    kamera.set(4, heigth)

cozunurluk_1080p()

def scalalama(frame, percent = 75):
    width = int(frame.shape[1]*percent/100)
    heigth = int(frame.shape[0]*percent/100)
    boyut = (width,heigth)
    return cv2.resize(frame, boyut, interpolation=cv2.INTER_AREA)

while True:
    ret, frame = kamera.read()
    frame75 = scalalama(frame, 15)
    cv2.imshow('480p Goruntu', frame)
    cv2.imshow('Goruntu', frame75)

    if cv2.waitKey(0) & 0xFF == ord('q'):  # qya basınca kapanıyor
        break

kamera.release()
cv2.destroyAllWindows()
