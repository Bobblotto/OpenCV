import cv2

video = cv2.VideoCapture(0)

while True:
    active, frame = video.read()
    edge = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.GaussianBlur(edge, (1, 1), 0.5)
    edge = cv2.Canny(edge, 70, 250)
    cv2.imshow("video", edge)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()