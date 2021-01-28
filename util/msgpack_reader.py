import numpy as np
import msgpack
import sys

def main(bin_fn, dest_fn):

	with open(bin_fn, "rb") as f:
	    data = msgpack.unpackb(f.read(), use_list=False, raw=False)

	a = data['landmarks']#.keys())

	b = (a['1'])  # os keys são os keyframes

	#print(b['pos_w'][0]) 

	#print(data['landmarks']['1']['pos_w'][0])
	for i in range (2,len(data['landmarks'])):
		if i in data['landmarks']:
			print(i)
			print(data['landmarks']['{}'.format(i)])

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 3:
        print("Unpack all landmarks in the map file and dump into a csv file")
        print("Each line represents position of landmark like \"x, y, z\"")
        print("Usage: ")
        print("    python pointcloud_unpacker.py [map file] [csv destination]")

    else:
        bin_fn = argv[1]
        dest_fn = argv[2]
        main(bin_fn, dest_fn)

#        /home/paulo/catkin_ws/openvslam/build/map.msg
#        /home/paulo/catkin_ws/openvslam/build/nome.csv

#o output é um dicionário:

#keys
#cameras
#frame_next_id
#key_frame_next_id
#keyframes
#landmarks_next_id
#landmarks

# Entender como está estruturado o banco de dados do msgpack