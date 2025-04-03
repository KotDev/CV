import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
iLastX = -1
iLastY = -1
while True:
    ret,frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_red = np.array([170,150,60])
    high_red = np.array([180,255,255])
    mask = cv.inRange(hsv, low_red,high_red)

    cv.erode(mask,mask,cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)))
    cv.dilate(mask,mask,cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)))
    cv.dilate(mask, mask, cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)))
    cv.erode(mask,mask,cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)))
    moment =cv.moments(mask)


    dm01=moment['m01']
    dm10=moment['m10']
    dArea=moment['m00']

    realArea = int(dArea//255)
    realm01 = int(dm01//255)
    realm10 = int(dm10//255)


    if realArea>500:

        posX = int(realm10//realArea)
        posY = int(realm01//realArea)
        if (iLastY>=0 and iLastX>=0):
            cv.rectangle(frame, (posX-int(np.sqrt(realArea)),posY-int(np.sqrt(realArea//2))), (posX+int(np.sqrt(realArea)),posY+int(np.sqrt(realArea))), (0,0,0), 3)
            cv.line(frame, (posX, posY), (iLastX, iLastY), (255,0,0), 2)

        iLastY=posY
        iLastX=posX
        print(realArea,posX,posY)

    cv.namedWindow('mask',cv.WINDOW_NORMAL)
    cv.namedWindow('res',cv.WINDOW_NORMAL)

    cv.imshow('res',frame)
    cv.imshow('mask',mask)
    if cv.waitKey(1) & 0xFF ==27:
        break
cap.release()
cv.destroyAllWindows()