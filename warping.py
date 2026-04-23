import cv2 as cv
import numpy as np

img = cv.imread("data/cards.jpg")

width,hight = 250,350

points1 = np.float32([[401,41],[561,132],[258,288],[420,380]])
points2 = np.float32([[0,0],[width,0],[0,hight],[width,hight]])

matrix = cv.getPerspectiveTransform(points1,points2)
imgout = cv.warpPerspective(img,matrix,(width,hight))

cv.imshow("img",img)
cv.imshow("out",imgout)
cv.waitKey(0)
cv.destroyAllWindows()