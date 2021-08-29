#!/usr/python3
import libtmux
import time


# video_path = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4'
video_list = ['/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4',
              '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste.MP4']
config_path = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/gopro.yaml'
vocab_path = '/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2'
map_path = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/maps'
video = '/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4'
# framesk = str(i)

windows = []
panes = []

for i, video_path in enumerate(video_list):
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
        f"rosrun publisher video -m {video_path} && tmux send-keys -t 3 C-c",
        "rosrun image_transport republish raw in:=/video/image_raw raw out:=/camera/image_raw",
        f"rosrun openvslam run_slam  \
        -v {vocab_path}  \
        -c {config_path} \
        --frame-skip 0 \
        --no-sleep \
        --auto-term \
        && tmux kill-session -t openvslam_tests; tmux wait-for -S command-finished"
    ]

    print(panes)
    for p, cmd in enumerate(command_list):
        panes[p].send_keys(cmd)
    server.attach_session("openvslam_tests")

# server.kill_server()
