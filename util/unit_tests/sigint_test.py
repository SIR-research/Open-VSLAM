import signal
import time
import sys
import subprocess
import os
# debugging  = True # If true, uses the same structure of the real, but with debugging data
# if debugging:
#     test = 'unit-test'
# base_path = '/home/paulo/openvslam/openvslam/build/'
# video_names = glob.glob(base_path+'/{}/videos/*.MP4'.format(test)) # Get video names list

# def handler(signum, frame):
#     print ('Here you go')
#     p.terminate
#     #takes 2 positional inputs
# signal.signal(signal.SIGINT, handler)

####### BASIC SOLUTION #########
p = subprocess.Popen(['rosrun','openvslam','cam_pose2pkl.py',
             'teste_sigint'
             ], preexec_fn= os.setsid)

pid = p.pid
time.sleep(2) 
 
kill_process =  subprocess.Popen(['kill', '{}'.format(pid)])
kill_process.terminate()


###################### CHECK WHEN THE SLAM SYSTEM STOPS RUNNING #################