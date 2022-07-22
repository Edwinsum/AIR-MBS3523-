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
    # img = cv2.imread('Resources/b3.jpeg')
    # img1 = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))  # resize img, o = row, 1 = column
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hueLow = cv2.getTrackbarPos('HL','MBS3523')
    # hueHigh = cv2.getTrackbarPos('HH', 'MBS3523')
    # satLow = cv2.getTrackbarPos('SL', 'MBS3523')
    # satHigh = cv2.getTrackbarPos('SH', 'MBS3523')
    # valueLow = cv2.getTrackbarPos('VL', 'MBS3523')
    # valueHigh = cv2.getTrackbarPos('VH', 'MBS3523')

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
            # print(cont)
            cv2.drawContours(img, [cont], -1, (0, 0, 255), 3) # [cont], data type, get data in 2d array[[],[],[]]
            arrX = []
            arrY = []
            for i in cont:
                arrX.append(i[0][0]) # i = [[x y]]
                arrY.append(i[0][1])
            # print(arrX)
            # print(arrY)
            maxX = max(arrX)
            minX = min(arrX)
            maxY = max(arrY)
            minY = min(arrY)
            # print(maxX, minX, maxY, minY)
            # print(arrY.index(maxY))
            maxYIndex = arrY.index(maxY)
            # print(arrX[maxYIndex])
            minYIndex = arrY.index(minY)
            # print(arrX[minYIndex])
            avgX = (maxX + minX)/2
            if avgX > arrX[maxYIndex] and avgX > arrX[minYIndex]:
                # print('left')
                if len(result) <= 10:
                    result.append('left')
            elif avgX < arrX[maxYIndex] and avgX < arrX[minYIndex]:
                # print('right')
                if len(result) <= 10:
                    result.append('right')
    # print(result)
    for j in result:
        # print(j)
        if j == 'left':
            countLeft+=1
        if j == 'right':
            countRight+=1
    if len(result) >= 10:
        if countLeft > countRight:
            # print('left')
            message = 'l'
        elif countLeft < countRight:
            # print('right')
            message = 'r'
        else:
            result = []
            message = ''
    if message != '':
        # print(message)
        text = message + '\r'
        ser.write(text.encode())
        print(text.encode())

    cv2.imshow('MBS3523', img)
    if cv2.waitKey(5) & 0xff == 27:
        break
    time.sleep(0.1)

cam.release()
cv2.destroyAllWindows()
