import cv2
import time
import os
from upload import *
import winsound

beep = winsound.Beep

cascPath = "haarcascade_upperbody.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    cv2.imshow("Frame", frame)
    if len(faces) > 0:
        beep(800, 1000)
        s, image = video_capture.read()
        im_name = str(time.time()) + '.jpg'
        path = "images"
        cv2.imwrite(os.path.join(path, im_name), image)
        file_loc = 'images/' + im_name
        cloud_loca = '/' + im_name
        print(im_name)
        if __name__ == '__main__':
            upload(file_loc, cloud_loca)
        time.sleep(15)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
