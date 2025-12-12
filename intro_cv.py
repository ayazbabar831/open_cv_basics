import cv2
cap = cv2.VideoCapture("data/Innocent Miku.mp4")

def rescale_frame(frame,scale=0.75):
    width = int(frame.shape[1] * scale )
    hight = int(frame.shape[0] * scale)
    dimension = (width,hight)
    
    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)

while True:
    success,img = cap.read()
    resized_img = rescale_frame(img)
    cv2.imshow("innocent miku",img)
    cv2.imshow("resized innocent miku",resized_img)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()