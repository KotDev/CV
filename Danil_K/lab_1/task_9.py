import numpy as np
from cv2 import VideoCapture
import cv2

capture = VideoCapture(0) # Подключаемся к камере телефона по ip webcam
while True:
    rate, frame = capture.read() # Считываем frame
    if not rate: # Проверяем что кадры не закончились
        break
    height, weight  = frame.shape[:2] # Получаем размер изображения
    center_x, center_y = weight // 2, height // 2 # Получаем координаты центрального пикселя
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Перекрашиваем frame в серый цвет
    matrix_radius = 200 // 2 # Получаем радиус матрицы
    y1 = center_y + matrix_radius # Получаем область выше центра по y
    y2 = center_y - matrix_radius # Получаем область ниже центра по y
    x1 = center_x + matrix_radius # Получаем область правее центра по x
    x2 = center_x - matrix_radius # Получаем область левее центра по x


    brightness = cv2.mean(gray[y2:y1, x2:x1])[0]# Получаем среднюю яркость области пикселей
    frame[y2:y1, x2:x1] = [brightness, brightness, brightness] # Перекрашиваем область

    cv2.imshow("display", frame) # Отображаем наш фрейм
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break