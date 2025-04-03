import cv2 as cv
import numpy as np

ip_cam = "http://10.155.81.74:8080/video"
cap = cv.VideoCapture(ip_cam)
n=50

while True:
    ret, frame = cap.read()
    h, w = frame.shape[:2]
    y = h//2 - n//2
    x = w//2 - n//2
    bright = np.mean(frame[y:y+n,x:x+n])
    frame[y:y+n,x:x+n]=bright
    cv.namedWindow('frame',cv.WINDOW_NORMAL)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF==27:
        break
cap.release()
cv.destroyAllWindows()