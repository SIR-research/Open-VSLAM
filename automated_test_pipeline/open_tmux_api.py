#!/usr/python3
import libtmux
import time
import os
import sys
import subprocess
import glob
import time
from typing import List

# TODO: replace by arg-parse
debugging = True
slam = True

# ***** Choose between the slam and localization task *****
if slam:
    task = 'slam'
else:
    task = 'localization'

base_path = '/home/paulo/Projects/openvslam_ws/openvslam/build/'
tests_ws_path = '/home/paulo/Projects/IC_SLAM_pipelines'

if debugging:
    test_type = 'experiment_data_debug'
    frameskip_list = [0]  # [0, 3]
    resolution_list = [720]  # [720, 1080]
else:
    frameskip_list = [0, 1, 3, 7]  # [0]  # [The objetive experiment
    test_type = 'experiment_data'
    resolution_list = [320, 480, 720, 1080]  # [720]


video_list = glob.glob(tests_ws_path+'/{}/videos/*.MP4'.format(test_type))
mask_list = glob.glob(tests_ws_path+'/{}/masks/*.png'.format(test_type))
config_path = tests_ws_path+'/{}/videos/gopro.yaml'.format(test_type)
map_path = tests_ws_path+'/{}/maps/'.format(test_type)
bag_path = tests_ws_path+'/{}/bags/'.format(test_type)
log_path = tests_ws_path+'/{}/logs/'.format(test_type)
vocab_path = '/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2'


print(video_list)
print(mask_list)
print(frameskip_list)
time.sleep(1)


for i, video_path in enumerate(video_list):
    # Name structure encoding: name-FPS-RESOLUTION-MASK

    resolution = video_path.split('-')[2]
    mask_valid: List[str] = []
    mask_names: List[str] = []

    # Filter valid masks
    for mask in mask_list:
        mask_name = mask.split('/')[-1]
        if(mask_name.startswith('mask{}'.format(resolution))):
            mask_valid.append(mask)
    # print(mask_valid)
    time.sleep(1)
    # Match the videos wich has the same resolution of the mask

    for mask in mask_valid[0]:
        for frameskip in frameskip_list:
            fps = int(120/(1+frameskip))

            # PARSE Map name / Mask
            # map_name = f'map_{direita/esquerda}-{fps}-{resolution}-{mask}'
            # print(f"map-{(video_path.split('/')[-1]).split("-")[:-1]}")
            map_name_args = ((video_path.split('/')[-1]).split("-")[:-1])
            print(map_name_args)
            map_name_suffix = (mask.split(".")[0]).split("-")[-1]
            # print(map_name_suffix)
            # map_name_args.append(map_name_suffix)
            map_name_args = [
                map_name_args[0], str(fps), map_name_args[2], map_name_suffix]
            map_name = f"map-{'-'.join(map_name_args)}.msg"
            # --- replace by a rosbag hehe
            bag_name = f"bag-{'-'.join(map_name_args)}-{task}.bag"
            log_name = f"log-{'-'.join(map_name_args)}-{task}.txt"

            print(map_name)
            print(bag_name)

            # # the tmux part
            windows = []
            panes = []
            server = libtmux.Server()
            session = server.new_session("openvslam_tests", window_name='win')

            win = session.new_window(window_name="win"+str(int(i/4)))
            windows.append(win)
            win.cmd('split-window', '-h')
            win.cmd('split-window', '-f')
            win.cmd('split-window', '-h')
            win.cmd('split-window', '-h')
            win.cmd('select-layout', 'tiled')

            panes.extend(win.list_panes())
            command_list = [
                "roscore",
                "rosrun image_transport republish raw in:=/video/image_raw raw out:=/camera/image_raw",
                f"stdbuf -oL rosrun openvslam run_{task}  \
                -v {vocab_path}  \
                -c {config_path} \
                --frame-skip {frameskip} \
                --no-sleep \
                --auto-term \
                --eval-log \
                --mask {mask} \
                --map-db {map_path+map_name} \
                &> {log_path+log_name} && \
                tmux kill-session -t openvslam_tests",
                f"rosrun publisher video -m {video_path} &&  tmux send-keys -t 4 C-c  && tmux send-keys -t 2 C-c && sleep 2",
                f"rosbag record -O {bag_path+bag_name} /clock /openvslam/camera_pose /openvslam/odometry /tf"
            ]

            print(panes)
            for p, cmd in enumerate(command_list):
                panes[p].send_keys(cmd)
                time.sleep(1)
            server.attach_session("openvslam_tests")
            time.sleep(1)
