import cv2
import os

image = cv2.imread('OpenCV2\\readimg\\newpfp.png')
gimage = cv2.imread('OpenCV2\\readimg\\newpfp.png', cv2.IMREAD_GRAYSCALE)

print(image)

cv2.imshow("Normal Image", image)
cv2.waitKey(0) # any keycode

b,g,r = cv2.split(image)

cv2.imshow("Red saturated Image", r)
cv2.waitKey(0)

cv2.imshow("Blue saturated Image", b)
cv2.waitKey(0)

cv2.imshow("Green saturated Image", g)
cv2.waitKey(0)

cv2.imshow("Grayscale Image", gimage)
cv2.waitKey(0)


os.chdir("OpenCV2\\readimg")
cv2.imwrite("GrayImage.png", gimage)