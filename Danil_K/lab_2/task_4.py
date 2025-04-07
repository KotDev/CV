import cv2
import numpy as np

from task_1 import get_hsv_image

lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

cv2.namedWindow("current img", cv2.WINDOW_NORMAL) # настраиваем текущее окно изображения
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)  # настраиваем текущее окно маски
cv2.namedWindow("result img", cv2.WINDOW_NORMAL) # настраиваем текущее окно изображение которое мы получим в результате
cv2.namedWindow("mask erode", cv2.WINDOW_NORMAL) # настраиваем текущее окно маски к которой была применина эррозия
cv2.namedWindow("mask dilate", cv2.WINDOW_NORMAL) # настраиваем текущее окно маски к которой было применино расширения


hsv, img = get_hsv_image("test2.png") # получаем изображения в формате hsv

mask_1 = cv2.inRange(hsv, lower_red1, upper_red1) # создаём маску первого диапазона красного цвета
mask_2 = cv2.inRange(hsv, lower_red2, upper_red2) # создаём маску второго диапазона красного цвета
mask = cv2.bitwise_or(mask_1, mask_2) # объединяем маску
karlen = np.ones((5, 5), np.uint8) # указываем кол-во закрашиваемых пикселей для ядра

erode_mask = cv2.erode(mask, karlen, iterations=3) # задаём эррозию для маски с итерацией 3
dilate_mask = cv2.dilate(mask, karlen, iterations=3) # задаём расширение для маски с итерацией 3

result_img = cv2.bitwise_and(img, img, mask=mask) # объединяем маски

moment = cv2.moments(dilate_mask, True) # получаем момент изображения
dm00 = moment["m00"] # находим кол-во белых пикселей
print(dm00 // 255) # получаем площадь изображения белых пикселей
cv2.imshow("current img", img) # выводим текущее изображение
cv2.imshow("mask", mask) # выводим изображение маски
cv2.imshow("mask erode", erode_mask) # выводим маску эррозии
cv2.imshow("mask dilate", dilate_mask) # выводим маску расширения
cv2.imshow("result img", result_img) # выводим результирующее изображение

cv2.waitKey(0)
cv2.destroyAllWindows()