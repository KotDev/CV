import cv2 as cv

def showImg(path):
    # IMREAD_GRAYSCALE - чб
    # IMREAD_REDUCED_GRAYSCALE_8 - чб и уменьшает в 8 раз
    # IMREAD_REDUCED_COLOR_4 - цветное и уменьшает в 4 раза
    img = cv.imread(path, cv.IMREAD_REDUCED_COLOR_4)
    # WINDOW_NORMAL - обычное окно, но с возможностью изменения размеров
    # оказывается с помощью или можно комбинировать флаги
    # WINDOW_GUI_EXPANDED - должен подрубать расширенный GUI интерфейс, но че то не заметно
    # WINDOW_FREERATIO - свободное изменение соотношения сторон
    cv.namedWindow("display",  cv.WINDOW_NORMAL | cv.WINDOW_FREERATIO | cv.WINDOW_GUI_EXPANDED)
    cv.imshow("display", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    showImg("./genius.png")