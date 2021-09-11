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

base_path = '/home/paulo/Projects/openvslam_ws/openvslam/build/'  # openvslam_path
tests_ws_path = '/home/paulo/Projects/IC_SLAM_pipelines'

if debugging:
    test_type = 'experiment_data_debug'
    frameskip_list = [0]  # [0, 3]
    resolution_list = [730]  # [720, 1080]
else:
    frameskip_list = [0, 1, 2, 3, 4, 5, 6]  # The objetive experiment
    test_type = 'experiment_data'
    resolution_list = [320, 480, 720, 1080]


video_list = glob.glob(tests_ws_path+'/{}/videos/*.MP4'.format(test_type))
mask_list = glob.glob(tests_ws_path+'/{}/masks/*.png'.format(test_type))
config_path = tests_ws_path+'/{}/videos/gopro.yaml'.format(test_type)
vocab_path = '/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2'
map_path = tests_ws_path+'/{}/maps/'.format(test_type)

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
    time.sleep(2)
    # Match the videos wich has the same resolution of the mask

    for mask in mask_valid:
        for frameskip in frameskip_list:
            fps = int(120/(1+frameskip))

            # PARSE Map name / Mask
            # map_name = f'map_{direita/esquerda}-{fps}-{resolution}-{mask}'
            # print(f"map-{(video_path.split('/')[-1]).split("-")[:-1]}")
            map_name_args = ((video_path.split('/')[-1]).split("-")[:-1])
            map_name_suffix = (mask.split(".")[0]).split("-")[-1]
            map_name_args.append(map_name_suffix)
            map_name = f"map-{'-'.join(map_name_args)}.msg"
            db_name = f"db-{'-'.join(map_name_args)}.pkl"

            print(map_name)
            print(db_name)

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

            panes.extend(win.list_panes())
            command_list = [
                "roscore",
                "rosrun image_transport republish raw in:=/video/image_raw raw out:=/camera/image_raw",
                f"rosrun openvslam run_slam  \
                -v {vocab_path}  \
                -c {config_path} \
                --frame-skip {frameskip} \
                --no-sleep \
                --auto-term \
                --eval-log \
                --mask {mask} \
                --map-db {map_path+map_name} \
                && tmux kill-session -t openvslam_tests",
                f"rosrun publisher video -m {video_path} && tmux send-keys -t 2 C-c"
            ]

            print(panes)
            for p, cmd in enumerate(command_list):
                panes[p].send_keys(cmd)
                time.sleep(1)
            server.attach_session("openvslam_tests")
            time.sleep(1)
