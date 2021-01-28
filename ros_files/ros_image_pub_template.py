#!/usr/bin/python

import rospy
from sensor_msgs.msg import Image

import cv2
import numpy as np
import time

#ROS Image message -> OpenCV2 IMAGE CONVERTER

from cv_bridge import CvBridge, CvBridgeError

#for delay measure
delay =0

bridge =CvBridge()

import sys
import signal

def img_callback(ros_data):
	global delta
	print(time.time(0*1000-delta))
	delta = (time.time()*1000)
	try:
		image_np = bridge.imgmsg_to_cv2(ros_data,"bgr8") ## mono8 já vai graysca
	except: CvBridgeError as e:
		print(e)
		cv2.imshow("output", image_np)

		
def main()
	rospy.init_node('image_listener')
	rospy.Subscriber("camera/rgb;image_raw", Image, img_callback, queue_size=1) ##Quanto menor, mais rapido

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting_down...')
	cv2.destroyAllWindows()

	if __name__ = '__main__':
		main()

#install TURTLEBOT3!