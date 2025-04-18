import cv2 as cv

def readVideoFromWebKam(path):
    video = cv.VideoCapture(0)
    ok, frame = video.read()
    w = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    writer = cv.VideoWriter(path, fourcc, fps, (w,h))
    while ok:
        cv.imshow("video", frame)
        writer.write(frame)
        ok, frame = video.read()
        if cv.waitKey(1) & 0xFF == 27: break
    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    readVideoFromWebKam("./output.mp4")
