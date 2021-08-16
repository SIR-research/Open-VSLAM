#!/bin/bash

while getopts m:v:c:s:f:k: flag
do 
    case "${flag}" in 
        m) map_path=${OPTARG};;
        v) vocab_path=${OPTARG};;
        c) config_path=${OPTARG};;
        s) video_path=${OPTARG};;
        f) frameskip=${OPTARG};;
        k) mask_path=${OPTARG};;
    esac
done

echo "vocab path: $vocab_path";
echo "config path: $config_path";
echo "map path : $map_path";
echo "video path: $video_path";
echo "frameskip : $frameskip";
echo "mask path : $mask_path";


# vocab_path=/home/paulo/Projects/openvslam_ws/openvslam/orb_vocab/orb_vocab.dbow2
# config_path=/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/gopro.yaml
# map_path='$tests_ws_path/experiment_data_debug/maps/mapa_debug.msg'
# video_path='/home/paulo/Projects/IC_SLAM_pipelines/experiment_data_debug/videos/direita-120-1080-teste2.MP4'
# mask_path='unknown'
# frameskip='1'
