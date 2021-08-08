import os
import sys
import subprocess
import glob
import os


base_path = '/home/paulo/openvslam/openvslam/build/'

resolution = 1080
mask_list = glob.glob(base_path+'/unit-test/masks/*.png')

mask_valid = []
for mask in mask_list:
    mask_name = mask.split('/')[-1]
    if(mask_name.startswith('mask{}'.format(resolution))):
        mask_valid.append(mask)
        print(mask_valid)
        print('\n')
# video_names = glob.glob(base_path+'/{}/videos/*.MP4'.format('testes')) 
# for video in video_names:
#     resolution = video.split('-')[2]
#     print(resolution)
