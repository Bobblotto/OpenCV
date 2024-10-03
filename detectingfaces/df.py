import cv2

group = cv2.imread("OpenCV2/detectingfaces/group.jpg")
groupg = cv2.cvtColor(group, cv2.COLOR_BGR2GRAY)
haar = cv2.CascadeClassifier("OpenCV2/detectingfaces/haarcascade_frontalface_default.xml")

faces = haar.detectMultiScale(groupg) # x, y, width, height

for person in faces:
    cv2.rectangle(group, (person[0], person[1]), (person[0]+person[2], person[1]+person[3]), (0, 0, 255), 2)

cv2.imshow("group", group)

cv2.waitKey(0)