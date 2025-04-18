import numpy as np
import cv2 as cv

def translateCamera(url, n):
    cap = cv.VideoCapture(url)

    ok, frame = cap.read()
    while ok:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        mean = int(gray.mean())
        h,w=frame.shape[:2]
        x1,y1 = w//2-n//2, h//2-n//2
        x2,y2 = w//2+n//2, h//2+n//2
        cv.rectangle(frame, (x1,y1), (x2,y2), (0,0,255),1)
        frame[y1:y2, x1:x2] = mean
        cv.namedWindow("Camera", cv.WINDOW_NORMAL)
        cv.imshow("Camera", frame)
        if cv.waitKey(1) & 0xFF == ord("q"): break
        ok, frame = cap.read()

    cv.destroyAllWindows()

if __name__ == "__main__":
    translateCamera("http://192.168.46.20:8080/video", 80)