import cv2 as cv

def showBGRandHSV(path):
    img = cv.imread(path)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.namedWindow("bgr", cv.WINDOW_FREERATIO)
    cv.namedWindow("hsv", cv.WINDOW_FREERATIO)
    cv.imshow("bgr", img)
    cv.imshow("hsv", hsv)
    print(hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    showBGRandHSV("./genius.png")
