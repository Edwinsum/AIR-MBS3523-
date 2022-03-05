# Save this file as OpenCV-Ex2-BounceBox.py
import random
import cv2
# import numpy as np
print(cv2.__version__)

# you may need to change the number inside () to 0 1 or 2,
# depending on which webcam you are using
capture = cv2.VideoCapture(0)
# Below 2 lines are used to set the webcam window size
capture.set(3, 640) # 3 is the width of the frame
capture.set(4, 480) # 4 is the height of the frame
success, img = capture.read()
size = 50
x = random.randint(0, 640 - 50)
dx = 5
y = random.randint(0, 480 - 50)
dy = 5

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.putText(img, 'MBS3523 Assignment 1b-Q3 Name: Sum Chung Chak', (30, 20), cv2.FONT_HERSHEY_PLAIN, 1.3, (200, 25, 100), 2)

    cv2.rectangle(img, (x, y), (x + size, y + size), (255, 255, 255), 3)
    x = x + dx
    y = y + dy
    if x >= 640 - size or x <= 0:
        dx = dx * (-1)
    if y >= 480 - size or y <= 0:
        dy = dy * (-1)


    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('0'):
        break

capture.release()
cv2.destroyAllWindows()
