import cv2
import numpy as np
from cv2 import VideoCapture

lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

capture = VideoCapture(0) # получаем доступ к веб камере

while True:
    rate, frame = capture.read() # считываем frame
    if not rate: # если закончились frame
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # переводим frame в hsv формат
    mask_1 = cv2.inRange(hsv_frame, lower_red1, upper_red1) # строим маску по первому диапазону красного
    mask_2 = cv2.inRange(hsv_frame, lower_red2, upper_red2) # строим маску по второму диапазону красного

    mask = cv2.bitwise_or(mask_1, mask_2) # объединяем маски
    karlen = np.ones((5, 5), np.uint8) # задаём эррозию для маски с итерацией 3
    erode_mask = cv2.erode(mask, karlen, iterations=1) # используем операцию эррозии на маску
    dilate_mask = cv2.dilate(mask, karlen, iterations=1) # используем операцию расширения на маску
    moment = cv2.moments(dilate_mask, True) # получаем момент изображения
    dm10 = moment["m10"] # получаем кол-во пикселей по x
    dm01 = moment["m01"] # получаем кол-во пиксерей по y
    dm00 = moment["m00"] # получаем общее кол-во белых пикселей
    if dm00 != 0: # провеяем что кол-во пикселй не равны из фильма
        x = dm10 // dm00 # получаем центр по x
        y = dm01 // dm00 # получаем центр по y
        p1 = (int(x + int(dm00 // 225 * 0.5)), int(y + int(dm00 // 255 * 0.5))) # получаем точку верхнего угла изображения
        p2 = (int(x - int(dm00 / 225 * 0.5)), int(y - int(dm00 // 255 * 0.5))) # получаем точку нижнего угла изображения
        cv2.rectangle(frame, pt1=p1, pt2=p2, color=(0, 0, 0), thickness=1, lineType=cv2.LINE_AA) # строим чёрный прямоугоьник
    cv2.imshow("mask dilate", frame) # отображаем frame
    if cv2.waitKey(1) & 0XFF == ord("q"): # ставим задержку в 1 мс и выход по нажатию клавиши q
        break
