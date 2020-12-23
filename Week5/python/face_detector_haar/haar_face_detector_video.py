# importing necessary packages
from imutils.video import VideoStream
import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


# initialize the video stream and allow camera sensor to warmup
# note - my camera is src 1, if you only have one camera on your
# device it is more likely to be 0
print("[INFO] starting video stream, please wait...")
cap = VideoStream(src=1).start()
time.sleep(3)

# loop over the frames from the video stream
while True:
    img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # show the output frame
    cv2.imshow('img',img)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, break from the loop
    if key == ord("q"):
        break

# cleanup and closing frame
cv2.destroyAllWindows()
cap.stop()