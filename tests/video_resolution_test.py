import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import glob
os.chdir("/home/paulo/openvslam/openvslam/build/testes/videos/")

print(os.getcwd())
print("Iniciando...")

nomes = glob.glob('*.MP4')

for nome in nomes:
    # cap =cv2.VideoCapture(nome)
    # width= cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # height= cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # fps= cap.get(cv2.CAP_PROP_FPS)
    # print("Video:{} - Dimensões  {},{} - {} FPS ".format(nome,width,height,fps))
    print("Video:",nome)
    os.system("ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {}".format(nome))
#\Check