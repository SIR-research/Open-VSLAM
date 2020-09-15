#!/bin/bash

#ffmpeg -i direita_trim.MP4 -filter:v fps=fps=30 direita_trim-30.MP4

#ffmpeg -i esquerda_trim.MP4 -filter:v fps=fps=60 esquerda_trim-60.MP4

#ffmpeg -i esquerda_trim.MP4 -filter:v fps=fps=30 esquerda_trim-30.MP4



cd /home/paulo/catkin_ws/openvslam-branch/build
./run_video_slam \
    -v ./orb_vocab/orb_vocab.dbow2 \
    -c ./testes/gopro.yaml \
    -m ./testes/direita_trim.MP4 \
    --no-sleep \
    --auto-term \
    --map-db ./testes/mapa_direita_trim.msg

ffmpeg -i direita_trim.MP4 -filter:v fps=fps=15 direita_trim-15.MP4

ffmpeg -i esquerda_trim.MP4 -filter:v fps=fps=15 esquerda_trim-15.MP4
