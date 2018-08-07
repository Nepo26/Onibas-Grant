import numpy as np
import cv2
import pyscreenshot as ImageGrab
import time



def procedure():
    last_time= time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 400, 400))) #x, y, w, h

        print('Look took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

       #img = cv2.imread("image.jpg")
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
