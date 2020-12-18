import os
import sys
import subprocess
import glob
import time
import signal

# **** Group subprocess function
def show_setting_prgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(os.getpgrp()))
    sys.stdout.flush()

# ***** Choose between the real data and debugging data *****
debugging  = True # If true, uses the same structure of the real, but with debugging data


if debugging:
    test = 'unit-test'
    frameskip_list = [0,3]
else: 
    frameskip_list = [0, 1, 2, 3, 4, 5, 6]  # The objetive experiment
    test = 'testes'
resolution_list = [320,480,720,1080] 

# **** Changing path to working dir and getting the video names ****
base_path = '/home/paulo/openvslam/openvslam/build/'
video_names = glob.glob(base_path+'/{}/videos/*.MP4'.format(test)) # Get video names list

# **** Calling roscore and image transport ****
subprocess.call(['gnome-terminal','--','roscore']) 
time.sleep(10)
subprocess.call(['gnome-terminal','--','rosrun','image_transport',
'republish','raw', 'in:=/video/image_raw','raw','out:=/camera/image_raw'])
time.sleep(1)

# **** Running openvslam in a loop ****
for video in video_names: 
    for mask in mask_list:
        for frameskip in frameskip_list:
            video_path = base_path+'/aist_living_lab_1/video.mp4' #TODO: Deixar os videos dinamicamente 
            resolution = video_names.split('-')[2]
            # The resolution is encoded at the 3° argument of video names: eg: left-FPS-RESOLUTION-MASK
            mask_list = glob.glob(base_path+'/{}/masks/*mask{}'.format(test,resolution))
            #Use only the masks that match the resolution

            # Call video publisher node
            subprocess.call(['gnome-terminal','--', 'rosrun','publisher','video',
            '-m','{}'.format(video_path)])


            time.sleep(5)
            #Call ROS Odometry to .pkl node 
            subprocess.call(['gnome-terminal','--','rosrun','openvslam','cam_pose2pkl.py',
            video.rsplit( ".", 1 )[ 0 ]
            ]) # the last arg takes off the file ext. to change it to .pkl
            # TODO: Interface the .pkl name as input as well, equal to the map name
            
            #OpenVSLAM file paths 
            vocab_path  = base_path+'/orb_vocab/orb_vocab.dbow2'
            config_path = base_path+'testes/videos/gopro.yaml'  #TODO: Change the path to gopro
            map_path    = base_path+'/{}/{}.msg'.format{test, map_name} #TODO: Change the path dynamically
            # The map will be saved into another folder, just like the db

            # db-filename = 
            # # TODO: Change 'filename' to the video names
            # c = subprocess.Popen(['rosrun openvslam node-python.py -filename'], \
            # shell=True, preexec_fn= os.setsid)

            subprocess.call(['gnome-terminal','--', 'rosrun', 'openvslam', 'run_slam',
                '-v', '{}'.format(vocab_path),
                '-c', '{}'.format(config_path),
                '--map-db', '{}'.format(map_path),
                'frame-skip {}'.format(frameskip),
                '--no-sleep',
                '--auto-term'
                ])

            print("SLAM process has finished for {}".format(video))

            # Kill the nodes and go to next iteration
            time.sleep(15)
            os.killpg(os.getpgid(c.pid), signal.SIGTERM)  # Send the signal to all the process groups

#run the slam system until it reaches a predefined state

#saves the whole stream of data from ros_odometry: -> at node-python script

# add conditions based on this stream.

#save into a parsable file, like a pandas dataframe, or a dict to dump and load, # check the idea 
#or either a csv file -> saving into a dump file


# Reference: https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
#            https://openvslam.readthedocs.io/en/master/ros_package.html