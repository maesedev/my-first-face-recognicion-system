import cv2
import os
import numpy 

faceClasify = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread('ahuevo/wilches.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

faces = faceClasify.detectMultiScale(image, 
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30,30),
    maxSize = (800,800))

for (x,y,w,h) in faces:
    cv2.rectangle( image, (x,y), (x+w , y+h),  (200,0,0), 3)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#FUNCIONA HPTAAAAAAAAAAAAAAA