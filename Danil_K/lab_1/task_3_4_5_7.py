import cv2
from cv2 import VideoCapture, VideoWriter


def write_to_file(cap: VideoCapture) -> None: # функция для записи видео в файл
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # задаём ширину видео
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # задаём высоту видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # создаем кодек для записи видео в файл
    video_writer = VideoWriter("/video/output.mov", fourcc, 25, (w,h)) # создаём класс для записи видео в файл
    while True:
        ret, frame = cap.read() # считываем изображения с камеры
        cv2.imshow("frame", frame) # отображаем frame
        video_writer.write(frame) # записываем frame в файл
        if cv2.waitKey(10) & 0xFF == ord('q'): # задержка в 10мс и при нажатии кнопки q выходим из программы
            break

def show_camera(cap: VideoCapture) -> None: # функция для показа видео с вебки
    while True:
        rate, frame = cap.read() # считывем frame
        if not rate:
            return
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # задаём серый цвет фрейму
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # задаём hsv цвет фрейму
        cv2.imshow("frame_gray", gray_frame) # отображаем frame окрашенный в серый цвет
        cv2.imshow("frame", frame) # Отображаем просто frame в окне
        cv2.imshow("frame_hsv", hsv) # отображаем фрейм в виде hsv
        if cv2.waitKey(10) & 0xFF == ord('q'): # задержка в 10мс и при нажатии кнопки q выходим из программы
            return

capture = VideoCapture(0) # создаём класс для подключения к вебкамере
show_camera(capture) # вызываем функцию отображения камеры на экран

# освобождаем ресурсы
capture.release()
cv2.destroyAllWindows()

