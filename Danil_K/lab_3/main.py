import math
import cv2
import numpy as np

img = cv2.imread("images/test2.png", flags=1) # Считываем изображение
cv2.namedWindow("blurred", cv2.WINDOW_NORMAL) # Настраиваем окно для ручного размытия
cv2.namedWindow("blurred2", cv2.WINDOW_NORMAL) # Настравиваем окно для размытия через OpenCV
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Переводим фото в серый
height, width = img_gray.shape[:2] # находим высоту и шириину изображения
kernel = np.zeros((5, 5)) # создаём нулевую матрицу ядра
matrix_radius = (kernel.shape[:2][0] - 1) // 2 # получаем радиус матрицы ядра
center_x = width // 2 # находим центр по x
center_y = height // 2 # находим центр по y

blurred_img = np.zeros_like(img_gray) # создаём нулевую матрицу размерности нашего изображения

def gauss_kernel(sigma): # функция вычисления ядра
    for y in range(kernel.shape[0]):
        for x in range(kernel.shape[0]):
            ct_y = y - matrix_radius # находим x относительно сентра матрицы
            ct_x = x - matrix_radius # находим y относительно сентра матрицы
            kernel[y, x] = (1 / (2 * math.pi * sigma)) * math.e ** (-1 * (ct_x**2 + ct_y**2) / (2 * sigma ** 2)) # заполняем ядро формулой Гауса

def normalize(): # функция нормализации ядра
    sum_elem = np.sum(kernel) # получаем сумму элементов ядра
    # делим каждый элемент ядра на сумму всех элементов ядра
    return kernel / sum_elem

gauss_kernel(1) # создаём ядро
normalize() # нормализируем ядро

blurred_img2 = cv2.GaussianBlur(img_gray, (7,7), 1) # создаём размытие при помощи OpenCV

for y in range(matrix_radius, height - matrix_radius): # проходимя по изображению по оси y учитывая радиус матрицы
    for x in range(matrix_radius, width - matrix_radius): # проходимя по изображению по оси x учитывая радиус матрицы
        B = img_gray[y - matrix_radius:y + matrix_radius + 1, x - matrix_radius:x + matrix_radius + 1] # строим матрицу B по нашей матрице черно белого изображения
        blurred_img[y, x] = np.sum(B * kernel) # производим свёртку и закидываем в нашу матрицу размытия

cv2.imshow("blurred", blurred_img) # отображаем изображения которое размывали сами
cv2.imshow("blurred2", blurred_img2) # отображаем изображения которое размывали через OpenCV
cv2.waitKey(0)
cv2.destroyAllWindows()







