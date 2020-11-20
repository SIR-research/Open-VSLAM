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


# **** Changing path to working dir and getting the video names ****
base_path = '/home/paulo/openvslam/openvslam/build/'
os.chdir(base_path+'/testes/videos')
video_names = glob.glob('*.MP4') # Get video names


# **** Calling roscore and image transport ****
subprocess.call(['gnome-terminal','--','roscore']) 
time.sleep(10)
subprocess.call(['gnome-terminal','--','rosrun','image_transport',
'republish','raw', 'in:=/video/image_raw','raw','out:=/camera/image_raw'])
time.sleep(1)

# **** Running openvslam in a loop ****
for video in video_names: 
    frameskip =1

    video_path = base_path+'/aist_living_lab_1/video.mp4'
    subprocess.call(['gnome-terminal','--', 'rosrun','publisher','video',
    '-m','{}'.format(video_path)])

    time.sleep(5)
    subprocess.call(['gnome-terminal','--','rosrun','openvslam','get_cam_pose-python.py',
    video.rsplit( ".", 1 )[ 0 ]
    ]) # the last arg takes off the file ext. to change it to .pkl

    #OpenVSLAM paths 
    vocab_path = '/home/paulo/openvslam/openvslam/build/orb_vocab/orb_vocab.dbow2'
    config_path= '/home/paulo/openvslam/openvslam/build/aist_living_lab_1/config.yaml'  #TODO: Change the path
    map_path = '/home/paulo/openvslam/openvslam/build/testes/mapa_ros.msg'              #TODO: Change the path dynamically
    # The map will be saved into another folder, just like the db

    subprocess.call(['gnome-terminal','--', 'rosrun', 'openvslam', 'run_slam',
        '-v', '{}'.format(vocab_path),
        '-c', '{}'.format(config_path),
        '--map-db', '{}'.format(map_path),
        'frame-skip {}'.format(frameskip),
        '--no-sleep',
        '--auto-term'
        ])
    print("final do loop do video ",video)
    
    c = subprocess.Popen(['rosrun openvslam node-python.py -nome'], \
    shell=True, preexec_fn= os.setsid)

    time.sleep(15)
    os.killpg(os.getpgid(c.pid), signal.SIGTERM)  # Send the signal to all the process groups

#run the slam system until it reaches a predefined state

#saves the whole stream of data from ros_odometry: -> at node-python script

# add conditions based on this stream.

#save into a parsable file, like a pandas dataframe, or a dict to dump and load, # check the idea 
#or either a csv file -> saving into a dump file


# Reference: https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
#            https://openvslam.readthedocs.io/en/master/ros_package.html