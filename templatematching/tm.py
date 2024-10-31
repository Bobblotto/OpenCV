import cv2
import numpy as np

img = cv2.imread("OpenCV2/templatematching/whereswaldo.jpg")
waldo = cv2.imread("OpenCV2/templatematching/waldo.png")
h, w, c = waldo.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
#TM_CCOEFF - checks pixel values of 2 images to find similarities
#TM_CCOEFF_NORMED
#TM_CCORR
#TM_CCORR_NORMED
#TM_SQDIFF
#TM_SQDIFF_NORMED

for i in range(len(methods)):

    copy = img.copy()

    result = cv2.matchTemplate(copy, waldo, methods[i])
    
    minmax = cv2.minMaxLoc(result)

    topleft = minmax[3]
    bottomright = topleft[0] + w, topleft[1] + h

    cv2.rectangle(copy, topleft, bottomright, (0, 0, 255), 2)
    cv2.imshow(str(methods[i]), copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    """vslice = slice(topleft[1], bottomright[1])
    hslice = slice(topleft[0], bottomright[0])
    cropped = img[vslice, hslice]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    dark = np.zeros(img.shape, "uint8")
    #img = cv2.addWeighted(img, 0.3, dark, 0.7, 0)

    img[vslice, hslice] = waldo
    cv2.imshow(str(methods[i]),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""