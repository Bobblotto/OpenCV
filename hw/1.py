import cv2

img = cv2.imread("OpenCV2\\hw\\newpfp.png")
img2 = cv2.imread("OpenCV2\\hw\\newpfp.png")

b, g, r = cv2.split(img)

cv2.imshow("img", img)
cv2.waitKey(0)

cv2.imshow("b", b)
cv2.waitKey(0)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey.png", grey)
cv2.imshow("grey", grey)
cv2.waitKey(0)

add = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
cv2.imshow("add", add)
cv2.waitKey(0)

sub = cv2.subtract(img, img2)
cv2.imshow("sub", sub)
cv2.waitKey(0)