import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    camon, frame = video.read()
    if camon:
        frame = np.flip(frame, axis=1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([100, 40, 40])
        upper_red = np.array([100, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        
        lower_red = np.array([155, 40, 40])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        mask3 = mask1 + mask2
        
        red = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, np.ones((3, 3), int), iterations=2)
        red = cv2.dilate(red, np.ones((3, 3), int), iterations=1)

        nonred = cv2.bitwise_not(red)
        visible = cv2.bitwise_and(frame, frame, mask=nonred)

        cv2.imshow("Video", visible)
    if cv2.waitKey(1) == 32:
        break
