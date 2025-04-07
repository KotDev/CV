import cv2
import numpy as np

from task_1 import get_hsv_image

lower_red1 = np.array([0, 50, 50]) # Диапазон тёмно красного
upper_red1 = np.array([10, 255, 255]) # Диапазон светло красного
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])
cv2.namedWindow("current img", cv2.WINDOW_NORMAL) # настраиваем текущее окно изображения
cv2.namedWindow("mask", cv2.WINDOW_NORMAL) # настраиваем текущее окно маски
cv2.namedWindow("result img", cv2.WINDOW_NORMAL) # настраиваем текущее окно изображение которое мы получим в результате

hsv, img = get_hsv_image("test.jpg") # получаем изображение в hsv формате

mask_1 = cv2.inRange(hsv, lower_red1, upper_red1) # создаём маску превого диапазона красного
mask_2 = cv2.inRange(hsv, lower_red2, upper_red2) # создаём маску второго диапазона красного
mask = cv2.bitwise_or(mask_1, mask_2) # объединяем маски

result_img = cv2.bitwise_and(img, img, mask=mask) # Применяем масску к изображению

cv2.imshow("current img", img) # выводим текущее изображение
cv2.imshow("mask", mask) # выводим получившуюся в результате объединения маску
cv2.imshow("result img", result_img) # выводим результат чёрно белого изображения

cv2.waitKey(0)
cv2.destroyAllWindows()