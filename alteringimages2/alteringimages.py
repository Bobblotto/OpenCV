import cv2

img = cv2.imread("OpenCV2\\alteringimages2\\Untitled.jpg")

rows, cols = img.shape[0:2]

cv2.imshow("image", img)
cv2.waitKey(0)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image", grey)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv)
cv2.waitKey(0)

rot = cv2.getRotationMatrix2D((cols/2, rows/2) ,90, 1)
rot = cv2.warpAffine(img, rot, (cols, rows))
cv2.imwrite("rot.png", rot)
cv2.imshow("rotated image", rot)
cv2.waitKey(0)

rot = cv2.getRotationMatrix2D((cols/2, rows/2) ,45, 1)
rot = cv2.warpAffine(img, rot, (cols, rows))
cv2.imwrite("rot.png", rot)
cv2.imshow("rotated image", rot)
cv2.waitKey(0)

edged = cv2.Canny(img, 100, 200)
cv2.imshow("edge detected image", edged)
cv2.waitKey(0)

line = cv2.line(img, (0, 0), (cols//2, rows//2), (255, 0, 0), 10)
cv2.imshow("line", line)
cv2.waitKey(0)

rect = cv2.rectangle(img, (0, 0), (cols//2, rows//2), (0, 255, 0), 10)
cv2.imshow("rect", rect)
cv2.waitKey(0)

circle = cv2.circle(img, (cols//2, rows//2), 25, (0, 0, 255), -1)
cv2.imshow("circle", circle)
cv2.waitKey(0)

text = cv2.putText(img, "Hello!", (0, rows//2), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)
cv2.imshow("text", text)
cv2.waitKey(0)