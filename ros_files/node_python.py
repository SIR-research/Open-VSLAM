#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped
import pickle
import sys

def test_callback(camera_pose):
    print("recebi msg?")
    #camera_pose # verificar a estrutura do bicho pra facilitar a escrita
    print("Position X",camera_pose.pose.position.x) 
    print("Position Y",camera_pose.pose.position.y)
    print("Position Z",camera_pose.pose.position.z)
    dict={}
    dict["x"] = camera_pose.pose.position.x
    dict["y"] = camera_pose.pose.position.y
    dict["z"] = camera_pose.pose.position.z
    dict["x_r"] = camera_pose.pose.orientation.x
    dict["y_r"] = camera_pose.pose.orientation.y
    dict["z_r"] = camera_pose.pose.orientation.z
    dict["w_r"] = camera_pose.pose.orientation.w
    dict["secs"] = camera_pose.header.stamp.secs
    dict["nsecs"] = camera_pose.header.stamp.nsecs
    dict["seq"] = camera_pose.header.seq
    pose_data.append(dict)
    
def listener():
    rospy.init_node("python",anonymous=True)
    rospy.Subscriber("/openvslam/camera_pose",PoseStamped, test_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    if rospy.is_shutdown():
        map_name = sys.argv[1] # entrar com esse nome no "main runner"
        with open( map_name+'.pkl','wb') as f:
            print("Dumping the pose data: ")
            pickle.dump(pose_data,f)

if __name__ == '__main__':
    pose_data = []
    listener()
    