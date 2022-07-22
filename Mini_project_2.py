import cv2
import serial
import time
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200)
time.sleep(0.5) #wait 0.5s for serial connection
print(cv2.__version__)

def NIL(x):
    pass

cv2.namedWindow('MBS3523')

# define frame width and frame height
width = 1080
height = 720

cam = cv2.VideoCapture('/dev/video0')  # enable webcam capture and save to cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # set frame height[']

result = []
countLeft = 0
countRight = 0
message = ""
while True:
    success, img = cam.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(imgHSV,(0,0,0),(179,255,45))
    # print(mask1.shape)
    cv2.imshow('Mask 1', mask1)
    # mask2 = cv2.bitwise_not(mask1)
    # cv2.imshow('Mask 2', mask2)

    Contours, no_use = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cont in Contours:
        area = cv2.contourArea(cont) #get area of a contour
        (x,y,w,h) = cv2.boundingRect(cont)
        if area > 200:
            cv2.drawContours(img, [cont], -1, (0, 0, 255), 3) # [cont], data type, get data in 2d array[[],[],[]]
            arrX = []
            arrY = []
            for i in cont:
                arrX.append(i[0][0]) # i = [[x y]]
                arrY.append(i[0][1]
            maxX = max(arrX)
            minX = min(arrX)
            maxY = max(arrY)
            minY = min(arrY)
            maxYIndex = arrY.index(maxY)
            minYIndex = arrY.index(minY)
            avgX = (maxX + minX)/2
            if avgX > arrX[maxYIndex] and avgX > arrX[minYIndex]:
                if len(result) <= 10:
                    result.append('left')
            elif avgX < arrX[maxYIndex] and avgX < arrX[minYIndex]:
                if len(result) <= 10:
                    result.append('right')
    for j in result:
        if j == 'left':
            countLeft+=1
        if j == 'right':
            countRight+=1
    if len(result) >= 10:
        if countLeft > countRight:
            message = 'l'
        elif countLeft < countRight:
            message = 'r'
        else:
            result = []
            message = ''
    if message != '':
        text = message + '\r'
        ser.write(text.encode())
        print(text.encode())

    cv2.imshow('MBS3523', img)
    if cv2.waitKey(5) & 0xff == 27:
        break
    time.sleep(0.1)

cam.release()
cv2.destroyAllWindows()
