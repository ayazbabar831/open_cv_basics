import cv2 as cv
img = cv.imread("data/Elaina icons.jpeg",0)
width = 700
ratio = width/img.shape[1]
hight = int(width * ratio)
dim = (hight,width)
copy_img = img.copy()
cv.imshow("cropped img",copy_img[200:400,100:600])
resized_img = cv.resize(copy_img,dim,interpolation=cv.INTER_AREA)
cv.imshow("resized img",resized_img)
copy_img[int(img.shape[0]/4):int(img.shape[0]/2),int(img.shape[1]/4):int(img.shape[1]/2)] = 200
two_x_img = cv.resize(copy_img,None,fx=2,fy=2)
cv.imshow("changed pic",copy_img)
cv.imshow("2x img",two_x_img)
fliped_img1 = cv.flip(copy_img,1)
fliped_img2 = cv.flip(copy_img,-1)
fliped_img3 = cv.flip(copy_img,0)
cv.imshow("fliped image",fliped_img1)
cv.imshow("fliped image3",fliped_img3)
cv.imshow("fliped image2",fliped_img2)

cv.waitKey(0)