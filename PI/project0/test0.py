import io
import cv2
import numpy as np
import pyscreenshot as ImageGrab

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Convert the picture into a numpy array
def process() :
    image = np.array(ImageGrab.grab(bbox=(0, 40, 600, 400)))

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/home/henrique/code/PI/henrique.xml')

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(image, 1.1, 5)


    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

    return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
