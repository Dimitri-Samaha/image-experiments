import cv2
import numpy as np

# Load cascade (face library)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def scan_filter(cap):
    ret, img = cap.read()
    h, w = img.shape[:2]
    y = 0
    while 1:
        ret, img = cap.read()
        cv2.line(img, (0,y), (w, y), (0, 0, 0), 5)
        if y == h:
            before = y
            y -= 2
        elif y == 0:
            before = y
            y += 2
        elif before > y:
            before = y
            y -= 2
        else:
            before = y
            y += 2

        cv2.imshow('img', img)
        key = cv2.waitKey(1)

        if key == 27:
            break



def scan_faces(img):
    # Detect Facess
    faces = face_cascade.detectMultiScale(img, 1.1, 1)

    w = img.shape[1]

    for (x, y, l, h) in faces:
        if x + int(l/2) >= w/2:
            cv2.rectangle(img, (x,y), (x+l, y+h), (255, 0, 0), 2)
        else:
            cv2.rectangle(img, (x,y), (x+l, y+h), (0, 0, 255), 2)
    return img

def blurr_faces(img):
    # Detect Facess
    faces = face_cascade.detectMultiScale(img, 1.1, 1)

    for (x, y, w, h) in faces:
        w -= 16
        h += 16
        blurr = img[y:y+h, x:x+w]
        blurr = cv2.GaussianBlur(blurr, (0, 0), 8)
        img[y:y+h, x:x+w] = blurr
    return img


def black_and_white(img):
    s = 0
    for i in range(3):
        s = np.array(img[:, :, i], dtype=np.uint16)
        s += s

    avrg = s / 3

    for i in range(3):
        img[:, :, i] = avrg

    return img

def default(img):
    return img

def compute_image_from_webcam():

    cap = cv2.VideoCapture(0)
    func_List = [default, black_and_white, scan_faces, blurr_faces, scan_filter]
    f = int(input("Default[0], Black and white[1], Scan faces[2], Blurr faces[3], Scan filter[4] "))
    f = func_List[f]
    if f != scan_filter:
        while 1:
            ret, img = cap.read()

            cv2.imshow('img', f(img))
            key = cv2.waitKey(1)

            if key == 27:
                break
    
    else:
        scan_filter(cap)

compute_image_from_webcam()
