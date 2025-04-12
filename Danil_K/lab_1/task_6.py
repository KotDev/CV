import cv2

img = cv2.imread(filename="images/img.jpeg", flags=1) # считываем картинку в виде матрицы
height, width = img.shape[:2] # получаем ширину и высоту картинки
center = (width // 2, height // 2) # находим центр картинки
cv2.namedWindow(winname='Display window', flags=cv2.WINDOW_NORMAL)

## перекладины
cv2.line(img, (center[0] + 50, center[1] + 5), (center[0] - 50, center[1] + 5), (0, 255, 0), 2) # верхняя перекладина
cv2.line(img, (center[0] + 50, center[1] - 5), (center[0] - 50, center[1] - 5), (0, 255, 0), 2) # нижняя перекладина

cv2.line(img, (center[0] + 5, center[1]-5), (center[0] + 5, center[1] - 50), (0, 255, 0), 2) # верхняя половино правой перекладины
cv2.line(img, (center[0] + 5, center[1] + 50), (center[0] + 5, center[1] + 5), (0, 255, 0), 2) # нижняя половина правой перекладины

cv2.line(img, (center[0] - 5, center[1] - 5), (center[0] - 5, center[1] - 50), (0, 255, 0), 2) # верхняя половина левой перекладины
cv2.line(img, (center[0] - 5, center[1] + 50), (center[0] - 5, center[1] + 5), (0, 255, 0), 2) # нижняя половина левой перекладины

# ребра креста
cv2.line(img, (center[0] + 5, center[1] - 50), (center[0] - 5, center[1] - 50), (0, 255, 0), 2) # верхнее ребро
cv2.line(img, (center[0] - 50, center[1] + 5), (center[0] - 50, center[1] - 5), (0, 255, 0), 2) # левое ребро
cv2.line(img, (center[0] + 5, center[1] + 50), (center[0] - 5, center[1] + 50), (0, 255, 0), 2) # нижнее ребро
cv2.line(img, (center[0] + 50, center[1] + 5), (center[0] + 50, center[1] - 5), (0, 255, 0), 2) # правое ребро


cv2.imshow("display", img) # отображаем крест
cv2.waitKey(0) # ставим задержку в 0 секунд
cv2.destroyWindow() # очищаем ресурсы