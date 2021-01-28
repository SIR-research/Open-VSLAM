
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import msgpack
import json
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from autolab_core import RigidTransform
import os
import cv2
import imageio





def main(bin_fn, video_path, dest_fn, plot):

    # Read file as binary and unpack data using MessagePack library
    with open(bin_fn, "rb") as f:
        data = msgpack.unpackb(f.read(), use_list=False, raw=False)

    # The point data is tagged "landmarks"
    key_frames = data["keyframes"]

    print("Point cloud has {} points.".format(len(key_frames)))

    key_frame = {int(k): v for k, v in key_frames.items()}

    if plot:
        x = []
        y = []
        z = []
        t = []
        for key in sorted(key_frame.keys()):
            point = key_frame[key]
            trans_cw = np.asarray(point["trans_cw"])
            rot_cw = np.asarray(point["rot_cw"])

            rigid_cw = RigidTransform(rot_cw, trans_cw)

            pos = np.matmul(rigid_cw.rotation, trans_cw)

            x.append(pos[0])
            y.append(pos[1])
            z.append(pos[2])
            t.append(float(point["ts"]))


        plt.xlabel('X')
        plt.ylabel('Y')
        plt.scatter(x, z)
        plt.show()

        plt.ylabel('Height')
        plt.xlabel('Time')
        plt.scatter(x=t, y=y)
        print(t)


        # # new a figure and set it into 3d
        fig = plt.figure()

        plt.show()

        
    else:
        # Write point coordinates into file, one point for one line
        with open(dest_fn, "w") as f:
            video_name = video_path.split("/")[-1][:-4]
            if not os.path.exists(video_name):
                os.mkdir(video_name)

            vidcap = cv2.VideoCapture(video_path)
            fps = int(vidcap.get(cv2.CAP_PROP_FPS)) + 1
            print(fps)
            count = 0

            for key in sorted(key_frame.keys()):
                point = key_frame[key]

                # position capture
                trans_cw = np.asarray(point["trans_cw"])
                rot_cw = np.asarray(point["rot_cw"])

                rigid_cw = RigidTransform(rot_cw, trans_cw)

                pos = np.matmul(rigid_cw.rotation, trans_cw)

                f.write("{}, {}, {}\n".format(pos[0], pos[1], pos[2]))

                vidcap.set(cv2.CAP_PROP_POS_FRAMES, fps * float(point["ts"]))


                # image capture
                success, image = vidcap.read()

                if not success:
                    print("capture failed")
                else:
                    cv2.imwrite(os.path.join(video_name, str(count) +".jpg"), image)

                count+=1




        print("Finished")


if __name__ == "__main__":

        bin_fn = '/home/paulo/catkin_ws/openvslam/build/mapa_direita.msg'
        video_path = '/home/paulo/catkin_ws/openvslam/build/testes/direita.MP4'
        dest_fn = '/home/paulo/catkin_ws/openvslam/build/try'
        main(bin_fn, video_path,dest_fn, plot=False)
