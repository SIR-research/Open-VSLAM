#!/bin/bash

#./run_video_slam -v ./orb_vocab/orb_vocab.dbow2 -m ./aist_living_lab_1/video.mp4 -c ./aist_living_lab_1/config.yaml --frame-skip 3 --no-sleep --map-db map.msg

#./run_video_slam -v (arg)(vocabulary file path) -m (arg)(video file path) -c (arg)(config file path) --m (arg)mask image path --frame-skip (interval frame skip)
#-- no-sleep (do not wait for next frame in real time) --auto-term (finish automaticaly viewer) --debug (debug mode) 
#--eval-log (store trajectory times for evaluation) -p,--map-db (arg)(store a map database at the path, after SLAM)
# How does the vocab interferes in the result? WHat information does it have? 
#Path do config file -- path to video -m = obrigatory, -- is optional?


###################################################################
#Rodar rápido diferentes --> 

#cd /home/paulo/catkin_ws/openvslam/build
cd /home/paulo/catkin_ws/openvslam-branch/build
# ./run_video_slam \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./aist_living_lab_1_m/config.yaml \
#     -m ./aist_living_lab_1_m/video.mp4 \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./aist_living_lab_1_m/fisheye_map.msg



# ./run_video_localization \
# 	-v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./aist_living_lab_1_m/config.yaml \
#     -m ./aist_living_lab_1_m/video.mp4 \
#     --frame-skip 3 \
#     --map-db ./aist_living_lab_1_m/fisheye_map.msg
# #--maping allows extend the prebuild map!!


##Para rodar no ROS --------------

#Tentando rodar o SLAM na câmera
# cd /home/paulo/OpenVSLAM/openvslam/build
# rosrun openvslam run_slam \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/Try_Paulo.yaml \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./map5.msg


# ./run_video_slam \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/Try_Paulo.yaml \
#     -m ./testes/Trajeto_Junior.mp4 \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./map5.msg


###    Rodando a GoPro    ###############################

# cd /home/paulo/OpenVSLAM/openvslam/build   
# ./run_video_slam \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/gopro.yaml \
#     -m ./testes/direita.MP4 \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./mapa_direita.msg




#Treinar em um e localizar em outro vídeo: Sucesso




########################### RUN LOCALIZATION #######################

#Escrever tutorial pra mim


#--maping  #allows extend the prebuild map!!



# rosrun openvslam run_localization \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/gopro.yaml \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./map5.msg
#    auto camera_pose=map_publisher_->get_current_cam_pose().inverse().eval();

# rosrun openvslam run_localization \
#    -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/webcam_config.yaml \
#     --map-db ./map2.msg



# ./run_video_localization \
# 	-v ./orb_vocab/orb_vocab.dbow2 \
#      -c ./aist_living_lab_1_m/config.yaml \
#      -m ./aist_living_lab_1_m/video.mp4 \
#          --frame-skip 3 \
#     --map-db ./map2.msg
# --maping allows extend the prebuild map!!


#  ./run_video_localization \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./aist_living_lab_1/config.yaml \
#     -m ./aist_living_lab_1/video.mp4 \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./aist_lab1_map.msg


# rosrun openvslam run_localization \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./aist_living_lab_1/config.yaml \
#     -m ./aist_living_lab_1/video.mp4 \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./aist_lab1_map.msg



	#With that, the results are improved =)



#The map file format is MessagePack, its reusable!

# ./run_video_slam -v ./orb_vocab/orb_vocab.dbow2 -m ./aist_living_lab_1_m/video.mp4 -c ./aist_living_lab_1_m/config.yaml --frame-skip 3 --no-sleep --map-db map.msg

# ./run_video_slam \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./fisheye_datasets/nu_eng2_corridor_3/config.yaml \
#     -m ./fisheye_datasets/nu_eng2_corridor_3/video.mp4 \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./map2.msg



# o que preciso saber:
# 1- Como salvar os mapas;  #Check
# 2- Como fazer os meus configs para o vídeo;  ##Check
### Como os parâmetros da câmera inteferem no resultado do processamento?  

# 3- Como aplicar isso de modo adequado;
# Testar agora com outros exemplos de fisheye


# ./run_video_localization \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/gopro.yaml \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./mapa_direita.msg


#Experimento: Inferir no mapa alheio


############################# ULTIMO ABERTO #################
# ./run_video_localization \
# 	-v ./orb_vocab/orb_vocab.dbow2 \
# 	-c ./testes/gopro.yaml \
# 	-m ./testes/video_1cut51.MP4 \
# 	--frame-skip 3 \
# 	--no-sleep \
# 	--auto-term \
# 	--map-db ./mapa_combo_4000.msg

# Obs: 0.306s de inferência -direita
# Obs: 0.327s de inferência - esquerda



# ./run_video_localization \
# 	-v ./orb_vocab/orb_vocab.dbow2 \
# 	-c ./testes/gopro.yaml \
# 	-m ./testes/direita.MP4 \
# 	--frame-skip 3 \
# 	--map-db ./mapa_combo_4000.msg
# ---------------------------------

 #Experimento: localizar em 10s dentro do mapa?
# Vamos ver os resulta

#video_cut1 -> ele encontra sim!
#video_cut2 -> LOST -20-30
#video_cut3 -> ele encontra sim! 30-40
#video_cut4 -> ele encontra sim! 40-50

#video_5cut3 -> ele encontra sim!* - 30/35s
#video_5cut4 -> LOST (da mesma forma que o 10s) 35/40s
#video_5cut5 -> ele encontra sim! - em menos de 1s 40/45s
#video_5cut6 -> ele encontra sim! - em menos de 1s 45/50s

# video_1cut6 -> 1s não foi suficiente - 45/46
# video_1cut5 -> Pegou da msm forma que o video video_5cut5 - 40/41
# video_1cut5 -> 1s não foi suficiente  - 41/42 

#--- Resposta: Parece que o alg. não foi capaz de dar conta


#Minhas observações: Não depende muito do tempo do vídeo para ele localizar
# Só depende se ele consegue um frame bom ou não





./run_video_slam \
	-v ./orb_vocab/orb_vocab.dbow2 \
	-c ./testes/gopro.yaml \
	-m ./testes/direita_trim.MP4 \
	--frame-skip 3 \
	--no-sleep \
	--auto-term \
	--map-db ./testes/mapa_teste.msg



#=============================== ROS ==========================#

# rosrun openvslam run_slam \
#     -v ./orb_vocab/orb_vocab.dbow2 \
#     -c ./testes/gopro.yaml \
#     --frame-skip 3 \
#     --no-sleep \
#     --auto-term \
#     --map-db ./mapa_ros.msg


#     # 