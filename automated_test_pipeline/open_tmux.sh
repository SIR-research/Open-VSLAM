#!/bin/sh

tmux source-file ~/.tmux.conf

tmux kill-pane -a


base_path='/home/paulo/Projects/openvslam_ws/openvslam/build'  # openvslam_path
tests_ws_path='/home/paulo/Projects/IC_SLAM_pipelines' # test scripts path

vocab_path=/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2
config_path=$tests_ws_path/experiment_data_debug/videos/gopro.yaml
map_path=$tests_ws_path/experiment_data_debug/maps/mapa_debug.msg

echo $vocab_path
echo $config_path
echo $map_path

# Split session into FOUR EQUAL quadrants
tmux new-session -s five_panes -n editor -d -c ~/code/five_panes '. install./source.zsh'

tmux selectp -t 0   # select the first (0) pane
tmux splitw -h -p 66 # split it into two halves
tmux splitw -h -p 50 # split it into two halves

tmux splitw -v -p 50   # split it into two halves

tmux selectp -t 1      # select the first (0) pane
tmux splitw -v -p 50   # split it into two halves

# tmux selectp -t 0      # select the first
# tmux splitw -v -p 50   # split it into two halves

tmux send-keys -t 0 'roscore' Enter

tmux selectp -t 1
tmux send-keys 'rosrun publisher video -m /home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4 && tmux send-keys -t 3 C-c' Enter  

# tmux send-keys 'tmux send-keys -t 3 C-c

tmux selectp -t 2
tmux send-keys 'rosrun image_transport republish raw in:=/video/image_raw raw out:=/camera/image_raw ' Enter

tmux selectp -t 3
tmux send-keys 'bash run_slam.sh && tmux kill-pane -a' Enter

tmux selectp -t 4
tmux send-keys '&& tmux send-keys -t 3 C-c

# tmux selectp -t 5
# tmux send-keys '' Enter
# tmux send-keys '' Enter