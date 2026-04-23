import cv2 as cv
import numpy as np

def getContours(img,img2):
    contours,hiearchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500 :
            print(area)
            # cv.drawContours(img2,cnt,-1,(0,0,255),3)
            peri = cv.arcLength(cnt,True)
            print(peri)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x,y,w,h = cv.boundingRect(approx)
            if len(approx)  == 3:
                cv.putText(img2,"triangle",(x+w,y+h),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
            
            cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),3)
            

img = cv.imread("data/shapes.jpg")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv.Canny(imgBlur,50,200)

getContours(imgCanny,img)



cv.imshow("img",img)
# cv.imshow("imgGray",imgGray)
# cv.imshow("imgBlur",imgBlur)
# cv.imshow("imgCanny",imgCanny)

cv.waitKey(0)


cv.destroyAllWindows()