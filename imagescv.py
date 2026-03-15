import cv2 as cv
import numpy as np

img = cv.imread("data/shrek.jpg")

cropped_img = img[100:400,50:400]
resize_img = cv.resize(img,(400,600))
print(img.shape)
cv.imshow("resized image",resize_img)
cv.imshow("orignal",img)
cv.waitKey(0)
cv.destroyAllWindows()