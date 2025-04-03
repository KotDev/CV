import cv2 as cv

def showVideo(path):
    video = cv.VideoCapture(path)
    while True:
        ok, frame = video.read()
        if not ok: break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("frame", gray)
        key = cv.waitKey(2)
        if key & 0xFF == 27: break
        elif key & 0xFF == ord(" "):
            if cv.waitKey(0) & 0xFF == ord(" "): continue


if __name__ == "__main__":
    showVideo("./video.mp4")