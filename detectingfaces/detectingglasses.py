import cv2

video = cv2.VideoCapture(0)

haar = cv2.CascadeClassifier("OpenCV2/detectingfaces/haarcascade_eye_tree_eyeglasses.xml")

while True:
    camon, frame = video.read()
    if camon:
        frameg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = haar.detectMultiScale(frameg, 1.1, 6)
        for person in faces:
            cv2.rectangle(frame, (person[0], person[1]), (person[0]+person[2], person[1]+person[3]), (0, 0, 255), 2)
        cv2.imshow("Video", frame)
    if cv2.waitKey(1) == 32:
        break