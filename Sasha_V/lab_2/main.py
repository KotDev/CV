import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
iLastX = -1
iLastY = -1
while True:
    ret,frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_red = np.array([170,150,60])
    high_red = np.array([179,255,255])
    mask = cv.inRange(hsv, low_red,high_red)
    binr = cv.threshold(mask,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    ker = np.ones((5,5),np.uint8)

    cv.erode(binr,ker,iterations=3)
    cv.dilate(binr,ker,iterations=3)
    cv.dilate(binr,ker,iterations=3)
    cv.erode(binr,ker,iterations=3)

    moment =cv.moments(binr)


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
            cv.rectangle(frame, (posX-int(np.sqrt(realArea)),posY-int(np.sqrt(realArea))), (posX+int(np.sqrt(realArea)),posY+int(np.sqrt(realArea))), (0,0,0), 3)
            cv.line(frame, (posX, posY), (iLastX, iLastY), (255,0,0), 2)

        iLastY=posY
        iLastX=posX
        print(realArea,posX,posY)

    cv.namedWindow('mask',cv.WINDOW_NORMAL)
    cv.namedWindow('res',cv.WINDOW_NORMAL)

    cv.imshow('res',frame)
    cv.imshow('mask',binr)
    if cv.waitKey(1) & 0xFF ==27:
        break
cap.release()
cv.destroyAllWindows()