#!/bin/bash
base_path='/home/paulo/Projects/openvslam_ws/openvslam/build'  # openvslam_path
tests_ws_path='/home/paulo/Projects/IC_SLAM_pipelines' # test scripts path

vocab_path=/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2
config_path=$tests_ws_path/experiment_data_debug/videos/gopro.yaml
map_path=$tests_ws_path/experiment_data_debug/maps/mapa_debug.msg

echo $vocab_path
echo $config_path
echo $map_path

rosrun openvslam run_slam  \
    -v $vocab_path  \
    -c $config_path \
    --map-db $map_path \
    --frame-skip 0 \
    --no-sleep \
    --auto-term