import numpy as np
import cv2
import pyscreenshot as ImageGrab
import time
from test0 import process



last_time= time.time()
while(True):

    cv2.imshow('window', process())

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
