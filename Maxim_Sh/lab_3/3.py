import numpy as np
import cv2 as cv

def gauss_ker(size, sigma = 1):
    ker = np.zeros((size, size))
    center = size // 2
    for i in range(size):
        for j in range(size):
            x, y = i - center, j - center
            ker[i, j] = np.exp(-(x**2 + y**2)/(2*sigma**2))
    return ker

def normalize(matrix):
    return matrix/np.sum(matrix)

def gauss_blur(image, kernel_size, sigma=1):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = gauss_ker(kernel_size, sigma)
    kernel = normalize(kernel)
    height, width = gray.shape
    copy = gray.copy()

    pad = kernel_size // 2
    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            val = gray[i-pad:i+pad+1, j-pad:j+pad+1]
            val = np.sum(val*kernel)
            copy[i][j] = val
    return copy

def gauss_blur_bgr(image, kernel_size, sigma=1):
    b,g,r = cv.split(image)
    kernel = gauss_ker(kernel_size, sigma)
    kernel = normalize(kernel)
    height, width = image.shape[:2]

    copy_list = []

    for color in [b,g,r]:
        copy = color.copy()

        pad = kernel_size // 2
        for i in range(pad, height - pad):
            for j in range(pad, width - pad):
                val = color[i-pad:i+pad+1, j-pad:j+pad+1]
                val = np.sum(val*kernel)
                copy[i][j] = val
        copy_list.append(copy)
    return cv.merge([copy_list[0],copy_list[1],copy_list[2]])


if __name__ == "__main__":
    img = cv.imread("./genius.png")
    blur_bgr = gauss_blur_bgr(img, 5, 1.5)
    blur_bgr_2 = cv.GaussianBlur(img, (5,5), 1.5,sigmaY=1.5)

    cv.namedWindow("original", cv.WINDOW_NORMAL)
    cv.namedWindow("blur_bgr", cv.WINDOW_NORMAL)
    cv.namedWindow("blur_bgr_2", cv.WINDOW_NORMAL)

    cv.imshow("original", img)
    cv.imshow("blur_bgr", blur_bgr)
    cv.imshow("blur_bgr_2", blur_bgr_2)

    cv.waitKey(0)
    cv.destroyAllWindows()

