#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


def talker(video):
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    
    rospy.init_node('video_publisher', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(30) 
    #keep publishing until a Ctrl-C is pressed

    bridge = CvBridge()

    while not rospy.is_shutdown():
        video_capture = cv2.VideoCapture(video)

        while(True):
            
            ret, frame = video_capture.read()

            
            try:
                pub.publish(bridge.cv2_to_imgmsg(frame,"bgr8")) 
            except CvBridgeError as e:
                print(e)
            except TypeError as e:
                print('No more images - video finished')
                break
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        #video ='/home/paulo/catkin_ws/openvslam-branch/build/testes/direita_trim.MP4'
        video ='/home/paulo/catkin_ws/openvslam-branch/build/aist_living_lab_1/video.mp4'
        talker(video)
    except rospy.ROSInterruptException:
        pass