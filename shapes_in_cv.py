import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv.line(img,(50,100),(100,200),(255,255,0),3)
cv.rectangle(img,(29,300),(10,100),(0,255,255),3)
cv.circle(img,(256,256),200,(0,150,255),3)
cv.putText(img,"HEAT ABNORMAL",(120,359),cv.FONT_HERSHEY_SIMPLEX,1,(0,59,255),3)

cv.imshow("img",img)
cv.waitKey(0)
img.release()
cv.destroyAllWindows()
