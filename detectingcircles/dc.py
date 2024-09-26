import cv2
import numpy as np

google = cv2.imread("OpenCV2\detectingcircles\google.png")
googleg = cv2.imread("OpenCV2\detectingcircles\google.png", 0)
googleb = cv2.blur(googleg, (5, 5))

hough = cv2.HoughCircles(googleb, cv2.HOUGH_GRADIENT, 1, 5, param1=60, param2=47, minRadius=20, maxRadius=40)
hough = np.uint(np.around(hough))

blob = cv2.SimpleBlobDetector_Params()

for row in hough:
    for circle in row:
        x, y, rad = circle
        cv2.circle(google, (x, y), rad, (0, 0, 255), 3)

cv2.imshow("img", google)

cv2.waitKey(0)