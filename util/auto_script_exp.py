import os
import sys
import subprocess
import glob
import time
from typing import List
import signal

#########
# **** Group subprocess function
# def show_setting_prgrp():
#     print('Calling os.setpgrp() from {}'.format(os.getpid()))
#     os.setpgrp()
#     print('Process group is now {}'.format(os.getpgrp()))
#     sys.stdout.flush()
# FOR NOW, UNUSED

# ***** Hardcoded control args *****
# TODO: replace by arg-parse
debugging = True
slam = True

base_path = '/home/paulo/Projects/openvslam_ws/openvslam/build/'  # openvslam_path
tests_ws_path = '/home/paulo/Projects/IC_SLAM_pipelines'

# '-s' / home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4 \

#config_path = tests_ws_path+'{}/videos/gopro.yaml'.format(test)
#map_path = tests_ws_path+'/{}/maps/{}.msg'.format(test, map_name)


# ***** Choose between the slam and localization task *****
if slam:
    task = 'slam'
else:
    task = 'localization'
# TODO: Define the differences between both of the pipelines (low priority)
# First step: only SLAM

# ***** Choose between the real data and debugging data *****

# It applies the same structure of the real, but with debugging data

if debugging:
    test_type = 'experiment_data_debug'
    frameskip_list = [0, 3]
    resolution_list = [720, 1080]
else:
    frameskip_list = [0, 1, 2, 3, 4, 5, 6]  # The objetive experiment
    test_type = 'experiment_data'
    resolution_list = [320, 480, 720, 1080]

# **** Changing path to working dir and getting the video names ****

# OpenVSLAM file paths
vocab_path = base_path+'/orb_vocab/orb_vocab.dbow2'
config_path = '/home/paulo/Projects/IC_SLAM_pipelines/' + \
    '{}/videos/gopro.yaml'.format('test-debug')
map_path = tests_ws_path+'/{}/maps/{}.msg'.format('test-debug', 'mapa_debug')

# Get video names list
video_names = glob.glob(tests_ws_path+'/{}/videos/*.MP4'.format(test_type))
mask_list = glob.glob(tests_ws_path+'/{}/masks/*.png'.format(test_type))

# **** Running openvslam in a loop ****
for video in video_names:

subprocess.Popen(['rosrun', 'openvslam',
                 'run_slam',
                  '-v', '{}'.format(vocab_path),
                  '-c', '{}'.format(config_path),
                  '--map-db', '{}'.format(map_path),
                  '--frame-skip {}'.format('0'),
                  '--no-sleep',
                  '--auto-term'
                  ])

# for i in range(2):
#     config_path = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/gopro.yaml'
#     vocab_path = '/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2'
#     map_path = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/maps'
#     video = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4'
#     framesk = str(i)

#     process = subprocess.Popen(['bash', 'open_tmux.sh',
#                                 '-v', '{}'.format(vocab_path),
#                                 '-c', '{}'.format(config_path),
#                                 '-m', '{}'.format(map_path),
#                                 '-s', '{}'.format(video),
#                                 '-k', '{}'.format('unknown'),
#                                 '-f', '{}'.format(framesk)
#                                 ])
# output, err = process.communicate()
# print(output)
# print(err)
# print("waiting")
#

# p = subprocess.Popen(['rosrun', 'openvslam', 'cam_pose2pkl.py',
#                         'teste_sigint'
#                         ], preexec_fn=os.setsid)
# SLAM_FINISHED = True
# ======================================================================================================================

# # Name structure encoding: name-FPS-RESOLUTION-MASK
# # Filter valid masks
# resolution = video.split('-')[2]
# mask_valid: List[str] = []
# mask_names: List[str] = [

# for mask in mask_list:
#     mask_name = mask.split('/')[-1]
#     if(mask_name.startswith('mask{}'.format(resolution))):
#         mask_valid.append(mask)
#         # Match the videos wich has the same resolution of the mask

# for mask in mask_valid:
#     for frameskip in frameskip_list:
#         # **** Configure the map name to save data ****
#         # The resolution is encoded at the third argument of video names
# fps = int(120/(1+frameskip))
#         mask_size = (
#             ((mask.rsplit(".", 1)[0]).split('/')[-1]).split('-')[-1])
#         file_name = ((video.rsplit(".", 1)[0]).split(
#             '/')[-1]).split('-')[0]
#         map_name_args = [file_name, str(
#             fps), str(resolution), str(mask_size)]
#         map_name = ('-').join(map_name_args)

#         # Call video publisher node
#         subprocess.call(['gnome-terminal', '--', 'rosrun', 'publisher',
#                          'video', '-m', '{}'.format(video)])

#         time.sleep(5)
#         # Call ROS Odometry to .pkl node
#         subprocess.call(['gnome-terminal', '--', 'rosrun', 'openvslam',
#                          'cam_pose2pkl.py',
#                          map_name
#                          ])
#         # The .pkl file will be saved with the same name as the map.

#         # The map will be saved into another folder, just like the pickle db

#         # c = subprocess.Popen(['rosrun openvslam node-python.py
#         #  -filename'], \
#         # shell=True, preexec_fn= os.setsid)

#         subprocess.call(['gnome-terminal', '--', 'rosrun', 'openvslam',
#                          'run_slam',
#                          '-v', '{}'.format(vocab_path),
#                          '-c', '{}'.format(config_path),
#                          '--map-db', '{}'.format(map_path),
#                          'frame-skip {}'.format(frameskip),
#                          '--no-sleep',
#                          '--auto-term'
#                          ])

#         p = subprocess.Popen(['rosrun', 'openvslam', 'cam_pose2pkl.py',
#                               'teste_sigint'
#                               ], preexec_fn=os.setsid)
#         pid = p.pid

#         SLAM_FINISHED = True

#         if(SLAM_FINISHED):
#             kill_process = subprocess.Popen(['kill', '{}'.format(pid)])
#             kill_process.terminate()

#         print("{} process has finished for {}.MP4".format(task, map_name))

#         # Kill the nodes and go to next iteration
#         time.sleep(10)

# ****  Code Guidelines ****

# os.killpg(os.getpgid(c.pid), signal.SIGTERM)
# Send the signal to all the process groups

# run the slam system until it reaches a predefined state

# saves the whole stream of data from ros_odometry: -> at node-python script

# add conditions based on this stream.

# save into a parsable file, like a pandas dataframe,
#  or a dict to dump and load,
# check the idea
# or either a csv file -> saving into a dump file


# Reference:
#   https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
#   https://openvslam.readthedocs.io/en/master/ros_package.html
