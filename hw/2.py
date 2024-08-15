import cv2

img = cv2.imread("OpenCV2\\hw\\g.png")
img2 = cv2.imread("OpenCV2\\hw\\g.png")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", grey)
cv2.waitKey(0)

edge = cv2.Canny(img, 200, 200)
cv2.imshow("img", edge)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("img", hsv)
cv2.waitKey(0)

line = cv2.line(img, (250, 250), (250, 150), (0, 255, 255), 5)
line = cv2.line(img, (250, 250), (150, 250), (0, 255, 255), 5)
line = cv2.line(img, (250, 250), (350, 250), (0, 255, 255), 5)
line = cv2.line(img, (250, 250), (350, 350), (0, 255, 255), 5)
line = cv2.line(img, (250, 250), (150, 350), (0, 255, 255), 5)

cv2.imshow("img", line)
cv2.waitKey(0)

line2 = cv2.line(img2, (250, 250), (275, 325), (0, 255, 255), 5)
line2 = cv2.line(img2, (275, 325), (350, 325), (0, 255, 255), 5)
line2 = cv2.line(img2, (350, 325), (300, 375), (0, 255, 255), 5)
line2 = cv2.line(img2, (300, 375), (325, 450), (0, 255, 255), 5)
line2 = cv2.line(img2, (325, 450), (250, 400), (0, 255, 255), 5)
line2 = cv2.line(img2, (250, 400), (175, 450), (0, 255, 255), 5)
line2 = cv2.line(img2, (175, 450), (200, 375), (0, 255, 255), 5)
line2 = cv2.line(img2, (200, 375), (150, 325), (0, 255, 255), 5)
line2 = cv2.line(img2, (150, 325), (225, 325), (0, 255, 255), 5)
line2 = cv2.line(img2, (225, 325), (250, 250), (0, 255, 255), 5)

cv2.imshow("img", line2)
cv2.waitKey(0)

text = cv2.putText(img2, "Hello!", (250, 250), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255))
                                
cv2.imshow("img", text)
cv2.waitKey(0)

rows, cols = img2.shape[0:2]

rot = cv2.getRotationMatrix2D((rows/2, cols/2), 90, 1)
rot =  cv2.warpAffine(img2, rot, (rows, cols))
cv2.imshow("img", rot)
cv2.waitKey(0)

rot = cv2.getRotationMatrix2D((rows/2, cols/2), 180, 1)
rot =  cv2.warpAffine(img2, rot, (rows, cols))
cv2.imshow("img", rot)
cv2.waitKey(0)

rot = cv2.getRotationMatrix2D((rows/2, cols/2), 270, 1)
rot =  cv2.warpAffine(img2, rot, (rows, cols))
cv2.imshow("img", rot)
cv2.waitKey(0)

rot = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 1)
rot =  cv2.warpAffine(img2, rot, (rows, cols))
cv2.imshow("img", rot)
cv2.waitKey(0)

rot = cv2.getRotationMatrix2D((rows/2, cols/2), 225, 1)
rot =  cv2.warpAffine(img2, rot, (rows, cols))
cv2.imshow("img", rot)
cv2.waitKey(0)