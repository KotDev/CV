import cv2 as cv

def task1(src):
    img = cv.imread(src)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.namedWindow("gray", cv.WINDOW_NORMAL)
    cv.imshow("gray", gray)
    blur = cv.GaussianBlur(gray, (5,5), 1.5,sigmaY=1.5)
    cv.namedWindow("blur", cv.WINDOW_NORMAL)
    cv.imshow("blur", blur)

if __name__ == "__main__":
    task1("../assets/genius.png")
    cv.waitKey(0)