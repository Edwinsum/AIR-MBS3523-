import cv2
import numpy as np

cam = cv2.VideoCapture(0)

def nil(x):
    pass

def nil1(y):
    pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('X_POS', 'MBS3523', 640, 640, nil)
cv2.createTrackbar('Y_POS', 'MBS3523', 480, 480, nil1)

while True:
    success, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1d-Q5 Name: Sum Chung Chak', (30, 20), cv2.FONT_HERSHEY_PLAIN, 1.3,
                (200, 25, 100), 2)
    width = int(cam.get(3))
    height = int(cam.get(4))

    x = cv2.getTrackbarPos('X_POS', 'MBS3523')
    y = cv2.getTrackbarPos('Y_POS', 'MBS3523')
    cv2.line(img, (x, 0), (x, height), (255, 0, 0), 2)
    cv2.line(img, (0, y), (width, y), (240, 140, 240), 2)

    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == ord('0'):
        break

cv2.destroyAllWindows()
