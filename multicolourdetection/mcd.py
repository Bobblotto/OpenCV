import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:

    active, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowred = np.array([140, 40, 40])
    upred = np.array([180, 255, 255])
    redmask = cv2.inRange(hsv, lowred, upred)

    lowblue = np.array([100, 80, 2]) 
    upblue = np.array([120, 255, 255])
    bluemask = cv2.inRange(hsv, lowblue, upblue)

    lowgreen = np.array([45, 50, 50])
    upgreen = np.array([80, 255, 255])
    greenmask = cv2.inRange(hsv, lowgreen, upgreen)

    dilatered = cv2.dilate(redmask, np.ones((3, 3), int))
    red = cv2.bitwise_and(frame, frame, mask=dilatered)

    dilateblue = cv2.dilate(bluemask, np.ones((3, 3), int))
    blue = cv2.bitwise_and(frame, frame, mask=dilateblue)

    dilategreen = cv2.dilate(greenmask, np.ones((3, 3), int))
    green = cv2.bitwise_and(frame, frame, mask=dilategreen)

    redcontours, n = cv2.findContours(dilatered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bluecontours, n = cv2.findContours(dilateblue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    greencontours, n = cv2.findContours(dilategreen, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for index, contour in enumerate(redcontours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 2)

    for index, contour in enumerate(bluecontours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 0), 2)
    
    for index, contour in enumerate(greencontours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()