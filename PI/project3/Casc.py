#import numpy as np
import cv2
import time
import imutils

cam =cv2.VideoCapture('http://192.168.15.16:8080/?action=stream')
time.sleep(2.0)
face_cascade = cv2.CascadeClassifier('/home/henrique/code/PI/project1/henrique.xml')
#last_time = time.time()
while True:
    ret, image = cam.read();

    frame_faces = imutils.resize(image, width=400)


#    faces = face_cascade.detectMultiScale(gray, 1.5, 5)




    gray = cv2.cvtColor(frame_faces,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    for (x,y,w,h) in faces:
        cv2.rectangle(frame_faces,(x,y),(x+w,y+h),(10, 225, 167),1)
        cv2.putText(frame_faces, "Pessoa", (x, y), cv2.FONT_HERSHEY_TRIPLEX,0.5, (10, 225, 167), 1)
    cv2.imshow('window', frame_faces)
    if cv2.waitKey(25) & 0xFF ==ord('q'):
        cv2.destroyAllWindows()
        break




    #print("Loop took {} seconds.".format(time.time()-last_time))
    #last_time = time.time()
