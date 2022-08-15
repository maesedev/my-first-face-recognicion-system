import cv2 
#funciona con una webcam nada más


capturadora = cv2.VideoCapture(0)
faceClasify = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = capturadora.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceClasify.detectMultiScale( grey , 1.2 , 5)
    for (x,y,w,h) in faces:
        cv2.rectangle( frame, (x,y), (x+w , y+h),  (200,0,0), 2 )
    cv2.imshow('frame',frame)
    if cv2.WaitKey(1) & 0xFF == ord('q'):
        break

capturadora.release()
cv2.destroyAllWindows()


#deberia de funcionar pero no se la vdd
