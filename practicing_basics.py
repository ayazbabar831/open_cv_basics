import cv2 as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)

cap = cv.VideoCapture("data/ball.mp4")
while True:
    success,img = cap.read()
    if not success:
        break
    resized_img = cv.resize(img,(640,480))
    # resized_gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
    # blur_img = cv.GaussianBlur(resized_img,(15,15),0)
    canny_image = cv.Canny(resized_img,50,150)
    dialate_img = cv.dilate(canny_image,kernel,iterations=1)
    # canny_image2 = cv.Canny(resized_img,100,150)
    # canny_image3 = cv.Canny(resized_img,150,150)
    
    cv.imshow("vid",dialate_img)
    # cv.imshow("vid2",canny_image2)
    # cv.imshow("vid3",canny_image3)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()    
