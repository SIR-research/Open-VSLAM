import os
import numpy as np
import sys

os.chdir("/home/paulo/openvslam/openvslam/build/testes/videos/")

lista1 =["1280:720","640:480"]# ,"480:320"]
lista2 = ["1280:720","640:480" ,"480:320"]
print(lista2)

print("Changing the video resolutions...")
 for res in lista1:
     name =  res.split(":")[1]
     os.system("ffmpeg -i direita-120-1080-none.MP4 -vf scale={} direita-{}-none.MP4".format(res,name))

 print("Videos direita - DONE")

for res in lista2:
    name =  res.split(":")[1]
    os.system("ffmpeg -i esquerda-120-1080-none.MP4 -vf scale={} esquerda-120-{}-none.MP4".format(res,name))

print("Videos esquerda - DONE")
