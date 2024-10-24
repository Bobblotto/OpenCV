import cv2
import numpy as np

img = cv2.imread("OpenCV2/templatematching/whereswaldo.jpg")
waldo = cv2.imread("OpenCV2/templatematching/waldo.png")
h, w, c = waldo.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

result = cv2.matchTemplate(img, waldo, methods[0])

minmax = cv2.minMaxLoc(result)

topleft = minmax[3]
bottomright = topleft[0] + w, topleft[1] + h

#cv2.rectangle(img, topleft, bottomright, (0, 0, 255), 2)
#cv2.imshow("img", img)
cv2.waitKey(0)

vslice = slice(topleft[1], bottomright[1])
hslice = slice(topleft[0], bottomright[0])
#cv2.imshow("cropped", cropped)
#cv2.waitKey(0)

dark = np.zeros(img.shape, "uint8")
img = cv2.addWeighted(img, 0.3, dark, 0.7, 0)

img[vslice, hslice] = waldo
cv2.imshow("add",img)
cv2.waitKey(0)

cv2.destroyAllWindows()