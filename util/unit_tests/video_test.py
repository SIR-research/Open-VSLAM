import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

print(os.getcwd())
os.chdir("//home//paulo//catkin_ws//openvslam//build//testes")
print(os.getcwd())

im = cv2.imread('direita.MP4')

import numpy as np
import cv2

cap = cv2.VideoCapture('direita.MP4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(np.shape(frame))


    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()