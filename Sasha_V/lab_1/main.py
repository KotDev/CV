import cv2 as cv

def print_cam():
    cap=cv.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        ret,frame = cap.read()
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',gray)
        if cv.waitKey(1) & 0xFF ==27:
            break
    cap.release()
    cv.destroyAllWindows()
def readIPWriteTOFile():
    video = cv.VideoCapture(0)
    ok, img = video.read()
    w = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    video_writer = cv.VideoWriter("output.mp4",fourcc,25,(w,h))
    while (True):
        ok, img = video.read()
        cv.imshow('img',img)
        video_writer.write(img)
        if cv.waitKey(1) & 0xFF == 27:
            break
    video.release()
    cv.destroyAllWindows()

def print_HSV():
    cap=cv.VideoCapture(0)
    while True:
        ret, frame= cap.read()
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        cv.namedWindow('hsv',cv.WINDOW_NORMAL)
        cv.imshow('hsv',hsv)
        if cv.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv.destroyAllWindows()

def HSV_explaine():
    frame = cv.imread("nix.jpg")
    if frame is None:
        print("Error")
    else:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    h,s,v = cv.split(hsv)
    cv.namedWindow('Hue', cv.WINDOW_NORMAL)
    cv.namedWindow('Saturation', cv.WINDOW_NORMAL)
    cv.namedWindow('Value', cv.WINDOW_NORMAL)
    cv.namedWindow('hsv', cv.WINDOW_NORMAL)
    cv.imshow('hsv',hsv)
    cv.imshow('Hue', h)
    cv.imshow('Saturation', s)
    cv.imshow('Value', v)
    cv.waitKey(0)

HSV_explaine()