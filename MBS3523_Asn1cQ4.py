import cv2
import numpy as np

# cam = cv2.VideoCapture('Resources/dog.mp4')
cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

while True:

    unuse, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1c-Q4 Name: Sum Chung Chak', (30, 20), cv2.FONT_HERSHEY_PLAIN, 1.3,
                (200, 25, 100), 2)
    frameGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.20, 4)
    # frameGray = cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    imgCrop = img[faces]
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frameGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frameGray = cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)
    frameGray[faces] = imgCrop

    cv2.imshow('Frame', img)
    # cv2.imshow('Framegray', imgCrop)
    cv2.imshow('1', frameGray)
    if cv2.waitKey(1) & 0xff == ord('0'):
        break

cam.release()
cv2.destroyAllWindows()
