import cv2 as cv
import numpy as np

video=cv.VideoCapture(0)
while True:
    ram,frame = video.read()
    h,w = frame.shape[:2]
    cent_w, cent_h = w//2, h//2

    b,g,r = frame[cent_h,cent_w]
    if(max(b,g,r)==b):
        cv.rectangle(frame, (cent_w - 100, cent_h - 10), (cent_w + 100, cent_h + 10), (255, 0, 0), -1)
        cv.rectangle(frame, (cent_w - 10, cent_h - 100), (cent_w + 10, cent_h - 10), (255, 0, 0), -1)
        cv.rectangle(frame, (cent_w - 10, cent_h + 10), (cent_w + 10, cent_h + 100), (255, 0, 0), -1)
    elif(max(b,g,r)==g):
        cv.rectangle(frame, (cent_w - 100, cent_h - 10), (cent_w + 100, cent_h + 10), (0, 255, 0), -1)
        cv.rectangle(frame, (cent_w - 10, cent_h - 100), (cent_w + 10, cent_h - 10), (0, 255, 0), -1)
        cv.rectangle(frame, (cent_w - 10, cent_h + 10), (cent_w + 10, cent_h + 100), (0, 255, 0), -1)
    elif(max(b,g,r)==r):
        cv.rectangle(frame, (cent_w - 100, cent_h - 10), (cent_w + 100, cent_h + 10), (0, 0, 255), -1)
        cv.rectangle(frame, (cent_w - 10, cent_h - 100), (cent_w + 10, cent_h - 10), (0, 0, 255), -1)
        cv.rectangle(frame, (cent_w - 10, cent_h + 10), (cent_w + 10, cent_h + 100), (0, 0, 255), -1)

    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
video.release()
cv.destroyAllWindows()

