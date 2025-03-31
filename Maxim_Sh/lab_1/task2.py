import cv2 as cv

def showImg(path):
    img = cv.imread(path)
    cv.namedWindow("display")
    cv.imshow("display", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    showImg("./genius.png")