import cv2 as cv
import numpy as np

def getContours(img, img2):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            corners = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            # Determine shape name
            if corners == 3:
                shape = "Triangle"
            elif corners == 4:
                aspect_ratio = w / float(h)
                shape = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
            elif corners == 5:
                shape = "Pentagon"
            elif corners == 6:
                shape = "Hexagon"
            else:
                # True circles have many corners after approximation
                shape = "Circle"

            cv.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv.putText(img2, shape, (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 1)
            
img = cv.imread("data/shapes.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(3,3),2)
canny = cv.Canny(blur,100,150,) 
getContours(canny,img)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()