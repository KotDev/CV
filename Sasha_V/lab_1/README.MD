Ответы на Вопросы:
1) В библиотеке OpenCV изображения представлены в виде 
многомерных массивов NumPy.
2) cv2.imshow("название", изображение) - Отображает изображение в окне с заданным именем
cv2.waitKey() - Ожидает нажатия клавиши и обрабатывает событие окон
cv2.destroiyAllWindows() - Закрывает всее окна openCV
3) В OpenCV управление параметрами окон (размер, положение, свойства) осуществляется через набор функций.
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)- окно с изменяемым размером
cv2.namedWindow("frame", cv2.WINDOW_FULLSCREEN) - полноэкранный режим и т.д.
4) За работу с видеопотоком отвечает класс cv2.VideoCapture
5) Получить видеопоток можно из Локальной камеры, Видеофайлов, Через IP камеры, Через захват экрана устройства
6) При работе с видеопотоками данные предоставляются в виде последовательных кадров(frame)
Frame - это один статический снимок из видеопотока, представленный в виде многомерного массива numpy
Метод read() выполняет две задачи: Захват следующего кадра и Возврат результата
7) Fourcc - это 4-х символьный идентификатор, используемый для обозначения кодеков, форматов данных или медиаконтейнеров.
Применяется для определения кодека, совместимости форматов, контроль качества видео
8) Класс VideoWriter используется для записи видеофайлов из последовательности кадров Вот его ключевые особенности:
Имя файла (например, output.avi, video.mp4).
FourCC-код — идентификатор кодека (см. FourCC).
FPS (кадровая частота) — количество кадров в секунду.
Разрешение видео — ширина и высота кадра.
Цветовой формат (опционально) — по умолчанию True (цветное изображение в BGR).
Пример: 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
9) Эта проверка используется для обработки нажатия клавиш в OpenCV, особенно для выхода из цикла по нажатию клавиши ESC.
cv2.waitKey(1) - через 1 миллисекунду и возвращает ascii-код нажатой клавиши
0xFF - обрезает все биты кроме младших 8, гарантирует, что мы получаем только младший байт, соответствующий ASCII-коду
== 27 - ASCII-код клавиши Esc
10) HSV (Hue, Saturation, Value) — альтернатива RGB для интуитивно понятного описания цвета. Он широко используется в:
Компьютерном зрении (цветовая сегментация, фильтрация),
Графических редакторах (регулировка оттенка/насыщенности),
Анализе изображений (выделение объектов по цвету).
Параметры HSV:
    Hue(тон) - Определяет цвет (0°–360°), но в OpenCV масштабируется до 0–180 для 8-бит.
    Saturation(насыщенность) - Интенсивность цвета (0 — серый, 255 — максимально насыщенный).
    Value(яркость) - Яркость цвета (0 — чёрный, 255 — максимальная яркость).
### Формулы преобразования RGB → HSV

Считаем, что:
- \( H \in [0, 360] \)
- \( S, V, R, G, B \in [0, 1] \)

Пусть:
- \( MAX = \max(R, G, B) \)
- \( MIN = \min(R, G, B) \)

#### 1. Вычисление тона (Hue):
\[
H = 
\begin{cases} 
0, & \text{если } MAX = MIN \ (\text{оттенок не определён}) \\
60 \times \dfrac{G - B}{MAX - MIN} + 0, & \text{если } MAX = R \text{ и } G \geq B \\
60 \times \dfrac{G - B}{MAX - MIN} + 360, & \text{если } MAX = R \text{ и } G < B \\
60 \times \dfrac{B - R}{MAX - MIN} + 120, & \text{если } MAX = G \\
60 \times \dfrac{R - G}{MAX - MIN} + 240, & \text{если } MAX = B 
\end{cases}
\]

#### 2. Вычисление насыщенности (Saturation):
\[
S = 
\begin{cases} 
0, & \text{если } MAX = 0 \\
1 - \dfrac{MIN}{MAX}, & \text{иначе}
\end{cases}
\]

#### 3. Вычисление яркости (Value):
\[
V = MAX
\]