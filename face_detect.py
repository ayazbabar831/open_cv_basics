import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier("data/haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)
while True:
    ret,frame = cap.read()
    frameflip = np.fliplr(frame)  
    imgGray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        imgGray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(20, 20),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv.rectangle(frameflip,(x,y),(x+w,y+h),(0,255,0),3)
    cv.imshow("img",frameflip)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()