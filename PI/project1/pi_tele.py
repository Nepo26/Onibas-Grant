import numpy as np
import cv2
import pyscreenshot as ImageGrab
import time
from tele_test import process



#Telegram



def process() :
    image = np.array(ImageGrab.grab(bbox=(0, 40, 600, 400)))

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/home/henrique/code/PI/project1/henrique.xml')

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(image, 1.1, 5)

    ##########################
    if len(faces) > 0:
        bot.sendMessage(PERSON, 'Uma face encontrada...')
    ##########################

    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

    return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

import telepot
bot = telepot.Bot('466963914:AAGJpIKVBG4Nc-tZagqDNeZ6g5U_lvAu50w')
time.sleep(5)
PERSON = bot.getUpdates()[0]['message']['from']['id']

last_time= time.time()
while(True):

    cv2.imshow('window', process())
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
