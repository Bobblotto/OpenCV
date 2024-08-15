import cv2
import os

img = cv2.imread("OpenCV2\\e\\Untitled.jpg")

b,g,r = cv2.split(img)

cv2.imshow("Img", img)
cv2.waitKey(0)

luvimg = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
cv2.imshow("LUV img", luvimg)
cv2.waitKey(0)

cv2.imshow("Green saturated img", g)
cv2.waitKey(0)

os.chdir("OpenCV2\\e")
cv2.imwrite("GreenSaturatedImg.png", g)