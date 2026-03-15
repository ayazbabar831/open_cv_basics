import cv2 as cv
import numpy as np

def empty(a):
    pass

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",640,240)
cv.createTrackbar("hue min","Trackbars",20,179,empty)
cv.createTrackbar("hue max","Trackbars",40,179,empty)
cv.createTrackbar("sat min","Trackbars",86,255,empty)
cv.createTrackbar("sat max","Trackbars",210,255,empty)
cv.createTrackbar("val min","Trackbars",46,255,empty)
cv.createTrackbar("val max","Trackbars",238,255,empty)


while True:
    img = cv.imread("data/shrek.jpg")
    resize_img = cv.resize(img,(640,480))
    resized_img_HSV = cv.cvtColor(resize_img,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("hue min","Trackbars")
    h_max = cv.getTrackbarPos("hue max","Trackbars")
    s_min = cv.getTrackbarPos("sat min","Trackbars")
    s_max = cv.getTrackbarPos("sat max","Trackbars")
    v_min = cv.getTrackbarPos("val min","Trackbars")
    v_max = cv.getTrackbarPos("val max","Trackbars")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    mask = cv.inRange(resized_img_HSV,lower,upper)
    


    # cv.imshow("R_img",resize_img)
    # cv.imshow("R_img_HSV",resized_img_HSV)
    # cv.imshow("mask",mask)
    result = cv.bitwise_and(resize_img,resize_img,mask=mask)
    cv.imshow("res",result)
    

    cv.waitKey(1)
cv.destroyAllWindows()

