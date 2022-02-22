import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 780)

while True:
    success, img = cam.read()
    print(success)
    cv2.imshow('210080499', img)
    if cv2.waitKey(5) & 0xff == ord('0'):
        break

cam.release()
cv2.destroyAllWindows()