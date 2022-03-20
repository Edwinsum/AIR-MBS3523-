import cv2
import numpy as np

drawing = False
point1 = []
point2 = []
coping = []
EVT = 0

def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing, EVT

    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = [x, y]
            EVT = event

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing is True:
            drawing = False
            point2 = [x, y]
            EVT = event

    elif event == cv2.EVENT_RBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = []
            EVT = event

    elif event == cv2.EVENT_RBUTTONUP:
        if drawing is True:
            drawing = False
            point2 = []
            EVT = event
            # frame[:, :] = frame
            # cv2.destroyWindow('cope')
        else:
            drawing = False

cam = cv2.VideoCapture(0)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)

while True:
    _, frame = cam.read()
    print(type(frame))
    if EVT == 4:
        if point1 and point2:
            cv2.rectangle(frame, point1, point2, (0, 255, 0))
            coping = frame[point1[1]:point2[1], point1[0]:point2[0]]
            cv2.imshow('cope', coping)

    if EVT == 5:
        frame[:, :] = frame
        cv2.destroyWindow('cope')
        EVT = 0

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
