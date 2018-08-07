import io
import cv2
import numpy as np

cam =cv2.VideoCapture('http://192.168.15.16:8080/?action=stream')
while(True):
         ret,img = cam.read();
         #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         cv2.imshow('window', img)
         cv2.waitKey(10)
