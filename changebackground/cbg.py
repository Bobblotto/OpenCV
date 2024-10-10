import cv2
import numpy as np

spongebob = cv2.imread("OpenCV2/changebackground/spongebob.jpg")
bg = cv2.imread("OpenCV2/changebackground/bg.jpg")

spongebob = cv2.resize(spongebob, (bg.shape[1], bg.shape[0]))

spongebobhsv = cv2.cvtColor(spongebob, cv2.COLOR_BGR2HSV)

lowergreen = np.array([45, 50, 50])
highergreen = np.array([80, 255, 255])

green = cv2.inRange(spongebobhsv, lowergreen, highergreen)
nongreen = cv2.bitwise_not(green)
print("green: ", green)
print("non-green: ", nongreen)

cv2.imshow("spongebob", nongreen)
cv2.waitKey(0)

spongebob = cv2.bitwise_and(spongebob, spongebob, mask=nongreen)

cv2.imshow("win", spongebob)
cv2.waitKey(0)

bg = cv2.bitwise_and(bg, bg, mask=green)

cv2.imshow("win", bg)
cv2.waitKey(0)

finished = cv2.addWeighted(spongebob, 1, bg, 1, 0)
cv2.imshow("done", finished)
cv2.waitKey(0)
