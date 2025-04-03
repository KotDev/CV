import cv2 as cv
import numpy as np


def crossImg(path):
    img = cv.imread(path)
    img_copy = img.copy()

    h, w = img.shape[:2]
    color = (0, 0, 0)
    thickness = 1
    width = 10
    mask_width = width + thickness
    size = min(w, h) // 4
    center_x = w // 2
    center_y = h // 2

    mask1 = np.zeros_like(img)
    mask2 = np.zeros_like(img)

    cv.rectangle(mask1, (center_x - mask_width, center_y - size),
                 (center_x + mask_width, center_y + size), (255, 255, 255), -1)
    cv.rectangle(mask2, (center_x - size, center_y - mask_width),
                 (center_x + size, center_y + mask_width), (255, 255, 255), -1)

    intersection = cv.bitwise_and(mask1, mask2)

    cv.rectangle(img, (center_x - width, center_y - size),
                 (center_x + width, center_y + size), color, thickness, cv.LINE_AA)
    cv.rectangle(img, (center_x - size, center_y - width),
                 (center_x + size, center_y + width), color, thickness, cv.LINE_AA)

    img[intersection == 255] = img_copy[intersection == 255]

    cv.imshow("Cross Without Intersection", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    crossImg("./genius.png")