import cv2
import numpy as np

spongebob = cv2.imread("OpenCV2/changebackground/spongebob.jpg")
spongebobhsv = cv2.cvtColor(spongebob, cv2.COLOR_BGR2HSV)
bg = cv2.imread("OpenCV2/changebackground/bg.jpg")

cv2.imshow("spongebob", spongebobhsv)
cv2.waitKey(0)

lowergreen = np.array([45, 50, 50])
highergreen = np.array([80, 255, 255])

green = cv2.inRange(spongebobhsv, lowergreen, highergreen)
nongreen = cv2.bitwise_not(green)
print("green: ", green)
print("non-green: ", nongreen)

cv2.imshow("spongebob", nongreen)
cv2.waitKey(0)

#spongebobr = cv2.resize(spongebob, (750, 750))
#bgr = cv2.resize(bg, (750, 750))

#added = cv2.addWeighted(spongebob, 0.5, bg, 0.5, 0)
#cv2.imshow("added img", added)
#cv2.waitKey(0)
