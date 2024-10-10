import cv2
import numpy as np

video = cv2.VideoCapture(0)

for i in range(60):
    camon, frame = video.read()
bg = frame
bg = np.flip(bg, axis=1)

while True:
    camon, frame = video.read()
    if camon:
        frame = np.flip(frame, axis=1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([0, 120, 50])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        
        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask3 = mask1 + mask2
        print(mask3)

        cv2.imshow("Video", frame)
    if cv2.waitKey(1) == 32:
        break