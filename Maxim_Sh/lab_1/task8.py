import cv2 as cv
import numpy as np

def crossImg(path):
    img = cv.imread(path)

    h, w = img.shape[:2]
    width = 10
    size = min(w, h) // 4
    center_x = w // 2
    center_y = h // 2

    b,g,r = img[center_y, center_x]

    if max(b,g,r) == b: color = (255,0,0)
    elif max(b,g,r) == g: color = (0, 255,0)
    elif max(b,g,r) == r: color = (0,0,255)
    else: color = (0,0,0)



    cv.rectangle(img, (center_x - width, center_y - size),
                 (center_x + width, center_y + size), color, -1, cv.LINE_AA)
    cv.rectangle(img, (center_x - size, center_y - width),
                 (center_x + size, center_y + width), color, -1, cv.LINE_AA)

    cv.imshow("Cross Without Intersection", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    crossImg("genius.png")