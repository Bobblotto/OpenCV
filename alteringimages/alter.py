import cv2

img = cv2.imread("OpenCV2\\alteringimages\\regpfp.png")
img2 = cv2.imread("OpenCV2\\alteringimages\\Untitled.jpg")

img = cv2.resize(img, (500, 500))
img2 = cv2.resize(img2, (500, 500))

addimg = cv2.addWeighted(img, 0.5, img2, 0.4, 0)

cv2.imshow("Added Image", addimg)
cv2.waitKey(0)

subimg = cv2.subtract(img, img2)

cv2.imshow("Subtracted Image", subimg)
cv2.waitKey(0)

borderimg = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=0)
cv2.imshow("Bordered Image", borderimg)
cv2.waitKey(0)

borderimg = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_REFLECT, value=0)
cv2.imshow("Bordered Image 2", borderimg)
cv2.waitKey(0)

