import cv2 as cv
import numpy as np

def task1(src):
    img = cv.imread(src)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.namedWindow("gray", cv.WINDOW_NORMAL)
    cv.imshow("gray", gray)
    blur = cv.GaussianBlur(gray, (5,5), 1.5,sigmaY=1.5)
    cv.namedWindow("blur", cv.WINDOW_NORMAL)
    cv.imshow("blur", blur)
    keni(blur)


def keni(img):
    Gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])

    height, width = img.shape
    pad = 1

    gradient_magnitude = np.zeros_like(img, dtype=np.float32)
    gradient_angle = np.zeros_like(img, dtype=np.float32)

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            region = img[i - pad:i + pad + 1, j - pad:j + pad + 1].astype(np.float32)

            grad_x = np.sum(region * Gx)
            grad_y = np.sum(region * Gy)

            gradient_magnitude[i, j] = np.sqrt(grad_x ** 2 + grad_y ** 2)

            tan = grad_y / grad_x
            if ((grad_x>0 and grad_y<0 and tan <-2.414) or (grad_x<0 and grad_y<0 and tan > 2.414)):
                gradient_angle[i,j] = 0
            elif (grad_x>0 and grad_y<0 and tan < -0.414):
                gradient_angle[i,j] = 1
            elif ((grad_x>0 and grad_y<0 and tan>-0,414) or (grad_x>0 and grad_y>0 and tan<0.414)):
                gradient_angle[i,j] = 2
            elif (grad_x>0 and grad_y>0 and tan<2.414):
                gradient_angle[i,j] = 3
            elif ((grad_x>0 and grad_y>0 and tan>2.414) or (grad_x<0 and grad_y>0 and tan < -2.414)):
                gradient_angle[i,j] = 4
            elif (grad_x<0 and grad_y>0 and tan<-0,414):
                gradient_angle[i,j] = 5
            elif ((grad_x<0 and grad_y>0 and tan>-0,414) or (grad_x<0 and grad_y<0 and tan < 0.414)):
                gradient_angle[i,j] = 6
            elif (grad_x<0 and grad_y < 0 and tg < 2.414):
                gradient_angle[i,j] = 7

    print(gradient_angle, gradient_magnitude)

if __name__ == "__main__":
    task1("../assets/genius.png")
    cv.waitKey(0)
    cv.destroyAllWindows()