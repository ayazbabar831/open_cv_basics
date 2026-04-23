import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)
while True:
    ret,frame = cap.read()
    
    lower_range = np.array([87,154,140])
    upper_range = np.array([110,255,255])
    frameflip = np.fliplr(frame).copy()

    blur_frame = cv.GaussianBlur(frameflip,(3,3),2)
    hsv_frame = cv.cvtColor(blur_frame,cv.COLOR_BGR2HSV)
    
    mask = cv.inRange(hsv_frame,lower_range,upper_range)
    
    kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(30,30))
    clean_mask1 = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel1)
    
    kernel2 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    clean_mask2 = cv.morphologyEx(clean_mask1,cv.MORPH_OPEN,kernel2)
    
    contours , hiearchy = cv.findContours(clean_mask2,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cnt_area = cv.contourArea(cnt)
        # largest = max(contours,key=cv.contourArea)
        if len(contours) > 0:
            x,y,w,h = cv.boundingRect(cnt)
            cv.rectangle(frameflip,(x,y),(x+w,y+h),(255,255,0),1)
    # cv.morphologyEx(mask,)
    
    bitwise_mask = cv.bitwise_and(frameflip,frameflip,mask=clean_mask2)
    
    
    
    
    
    
    
    cv.imshow("video",frameflip)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
cap.release()