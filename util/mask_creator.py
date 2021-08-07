import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Image resolutions
im1080p = (1080,1920,3)
im720p =  (1280,720)
im640p =  (480,640) 
im480p =  (320,480)

im1 = np.zeros(im1080p)
infLimY =int(0.2*im1.shape[0])
upLimY = im1.shape[0] - int(0.4*im1.shape[0])

#im1[infLimY:upLimY,0:im1.shape[1]] = 1

print(infLimY,upLimY)

cv2.namedWindow("image")
cv2.imshow("image", im1)
#plt.imshow(im1)
#plt.show()
cv2.imwrite('/home/paulo/openvslam/openvslam/build/testes/masks/mask-1080.bmp', im1)

im = im1
height,width,depth = im.shape
cv2.rectangle(im1,(384,0),(510,128),(0,255,0),3)
cv2.rectangle(rectangle,(width/2,height/2),200,1,thickness=-1)

masked_data = cv2.bitwise_and(im, im, mask=rectangle)

