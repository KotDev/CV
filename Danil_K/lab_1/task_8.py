import cv2
import numpy as np

img = cv2.imread(filename="images/img.jpeg", flags=1) # считываем картинку в виде матрицы
height, width = img.shape[:2] # получаем ширину и высоту картинки
center = (width // 2, height // 2) # находим центр картинки
cv2.namedWindow(winname='Display window', flags=cv2.WINDOW_NORMAL)
hsl_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS) # переводим картинку в hsl
h, l, s = hsl_img[center[0], center[1]] # получаем h s l значения центрального пикселя
color = (255, 0, 0)  # задаём синий цвет по умолчанию
if h == 0: # проверяем что это красный цвет
    color = (0, 0, 255) # задаём красный
elif 200 <= h < 120: # проверяем что это зеленый цвет
    color = (0, 255, 0) # задаём зеленый
else: # в притивном случае это красный
    color = color
mask = np.zeros((height, width), dtype=np.uint8) # cоздаем маску для заливки


points = np.array([
    # внешний контур
    [center[0]-50, center[1]-5],  # левый верх
    [center[0]-50, center[1]+5],   # левый низ
    [center[0]-5, center[1]+5],    # внутренний левый низ
    [center[0]-5, center[1]+50],   # нижний левый
    [center[0]+5, center[1]+50],   # нижний правый
    [center[0]+5, center[1]+5],    # внутренний правый низ
    [center[0]+50, center[1]+5],   # правый низ
    [center[0]+50, center[1]-5],   # правый верх
    [center[0]+5, center[1]-5],    # внутренний правый верх
    [center[0]+5, center[1]-50],   # верхний правый
    [center[0]-5, center[1]-50],   # верхний левый
    [center[0]-5, center[1]-5]     # внутренний левый верх
])

cv2.fillPoly(mask, [points], color=255) # заливаем область креста
img[mask == 255] = color  # делаем полную заливку по маске

## перекладины
cv2.line(img, (center[0] + 50, center[1] + 5), (center[0] - 50, center[1] + 5), (0, 0, 255), 2) # верхняя перекладина
cv2.line(img, (center[0] + 50, center[1] - 5), (center[0] - 50, center[1] - 5), (0, 0, 255), 2) # нижняя перекладина

cv2.line(img, (center[0] + 5, center[1]-5), (center[0] + 5, center[1] - 50), (0, 0, 255), 2) # верхняя половино правой перекладины
cv2.line(img, (center[0] + 5, center[1] + 50), (center[0] + 5, center[1] + 5), (0, 0, 255), 2) # нижняя половина правой перекладины

cv2.line(img, (center[0] - 5, center[1] - 5), (center[0] - 5, center[1] - 50), (0, 0, 255), 2) # верхняя половина левой перекладины
cv2.line(img, (center[0] - 5, center[1] + 50), (center[0] - 5, center[1] + 5), (0, 0, 255), 2) # нижняя половина левой перекладины

# ребра креста
cv2.line(img, (center[0] + 5, center[1] - 50), (center[0] - 5, center[1] - 50), (0, 0, 255), 2) # верхнее ребро
cv2.line(img, (center[0] - 50, center[1] + 5), (center[0] - 50, center[1] - 5), (0, 0, 255), 2) # левое ребро
cv2.line(img, (center[0] + 5, center[1] + 50), (center[0] - 5, center[1] + 50), (0, 0, 255), 2) # нижнее ребро
cv2.line(img, (center[0] + 50, center[1] + 5), (center[0] + 50, center[1] - 5), (0, 0, 255), 2) # правое ребро


cv2.imshow("display", img) # отображаем крест
cv2.waitKey(0) # ставим задержку в 0 секунд
cv2.destroyWindow() # очищаем ресурсы