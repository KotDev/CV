import cv2

img = cv2.imread(filename="images/img.jpeg", flags=0) # считываем изображение и перекрашиваем в серый цвет
cv2.namedWindow(winname='Display window', flags=cv2.WINDOW_NORMAL) # создаём окно отображения изображения
cv2.imshow(winname='Display window', mat=img) # отображаем полученное изображение
cv2.waitKey(0) # ставим задержку в 0 секунд
cv2.destroyWindow() # освобождаем ресурсы