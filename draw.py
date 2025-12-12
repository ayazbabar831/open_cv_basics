import cv2 as cv
import numpy as np

blank = np.zeros((500,700,3),dtype="uint8")
rectangle = cv.rectangle(blank,(0,0),(225,225),(0,255,0),-1)
cv.imshow("blank",rectangle)
blank[225:228,70:333] = 213, 223, 0
circle = cv.circle(blank,(225,225),40,(128,128,0),3)
line = cv.line(blank,(252,252),(400,300),(128,128,0),3)
cv.imshow("blank",line)
print(blank.shape[1])
blank_text = cv.putText(blank,"Hatsune Miku",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(170,128,10),1)
cv.imshow("blank text",blank_text)
cv.waitKey(0)