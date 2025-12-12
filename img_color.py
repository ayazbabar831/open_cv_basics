import cv2 as cv

img = cv.imread("data/Elaina icons.jpeg")

b,g,r = cv.split(img)
cv.imshow("elainab",b)
cv.imshow("elainag",g)
cv.imshow("elainar",r)
merged_channel =cv.merge((b,g,r))
cv.imshow("merged",merged_channel)
img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v = cv.split(img_hsv)
h = h+20
s = s+10
img_merge_hsv = cv.merge((h,s,v))
back_to_bgr = cv.cvtColor(img_merge_hsv,cv.COLOR_HSV2BGR)
cv.imshow("back to bgr",back_to_bgr)
cv.imshow("hsv",img_hsv)
cv.imshow("rgb",img_rgb)
cv.waitKey(0)