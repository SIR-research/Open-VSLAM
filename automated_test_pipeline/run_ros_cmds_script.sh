#!/bin/bash

roscore & \
rosrun image_transport republish raw in:=/video/image_raw raw out:=/camera/image_raw & \
sleep 5 & \
rosrun publisher video -m /home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4 & \
sleep 5 & \
rosrun openvslam run_slam  \
    -v $vocab_path  \
    -c $config_path \
    --map-db $map_db \
    --frame-skip 0 \
    --no-sleep \
    --auto-term


rosrun openvslam run_slam  \
    -v $vocab_path  \
    -c $config_path \
    --map-db $map_db \
    --frame-skip 0 \
    --no-sleep \
    --auto-term



# 'rosrun', 'openvslam',
#                      'run_slam',
#                       '-v', '{}'.format(vocab_path),
#                       '-c', '{}'.format(config_path),
#                       '--map-db', '{}'.format(map_path),
#                       'frame-skip {}'.format('0'),
#                       '--no-sleep',
#                       '--auto-term'
#                       ])

