import cv2 as cv
import numpy as np

def red_detect(url):
    cap = cv.VideoCapture(url)
    ok, frame = cap.read()
    cv.namedWindow("camera", cv.WINDOW_NORMAL)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])


    kernel = np.ones((5, 5), np.uint8)

    while ok:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        mask1 = cv.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv.inRange(hsv, lower_red2, upper_red2)
        mask = cv.bitwise_or(mask1, mask2)
        mask = cv.threshold(mask, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]

        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        contours, _ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv.contourArea(cnt)
            if area <= 500: continue
            moment = cv.moments(cnt)
            if moment['m00'] != 0:  # Проверка, что площадь не нулевая
                cx = int(moment['m10'] / moment['m00'])  # Центр X
                cy = int(moment['m01'] / moment['m00'])  # Центр Y
                cv.circle(frame, (cx, cy), 2, (0, 0, 0), -1)  # Рисуем точку
                x, y, w, h = cv.boundingRect(cnt)
                cv.rectangle(frame, (x,y), (x+w,y+h),(0,0,0), 1)

        cv.imshow("camera", frame)
        if cv.waitKey(1) & 0xFF == 27: break
        ok, frame = cap.read()

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    red_detect(0)
#ваши коментарии к коду отвратительны. через 2 месяца ты уже ничего не вспомнишь, приучи себя добавлять коментарии к мало мальски
#значмым вещам
