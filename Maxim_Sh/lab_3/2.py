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

if __name__ == "__main__":
    print(normalize(gauss_ker(3)))
    print(normalize(gauss_ker(5)))
    print(normalize(gauss_ker(7)))

